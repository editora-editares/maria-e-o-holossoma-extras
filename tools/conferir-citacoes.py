#!/usr/bin/env python3
"""Confere toda citacao literal dos materiais contra o fonte de ../mary-livro.

Este repositorio nao tem suite de testes: o equivalente a "teste" e fidelidade
ao livro. Este script e a parte automatizavel disso.

A convencao que ele depende, documentada em materiais/README.md:

    BLOCKQUOTE E CITACAO LITERAL DO LIVRO, E NADA MAIS.

Frase sugerida ao mediador, exemplo inventado ou fala hipotetica vao em
italico. Se um blockquote falhar aqui, ou a citacao esta errada, ou nao devia
ser blockquote.

Aceita o rotulo de locutor no inicio do bloco -- "**Maria:** "..."" -- porque
o livro compoe as falas com o nome fora das aspas.

Uso:  python3 tools/conferir-citacoes.py [caminho ...]
      sem argumento, confere materiais/ inteiro. Sai 1 se houver falha.
"""
import glob
import pathlib
import re
import sys

LIVRO = pathlib.Path(__file__).resolve().parent.parent.parent / "mary-livro"


def fonte_do_livro() -> str:
    if not LIVRO.is_dir():
        sys.exit(f"erro: {LIVRO} nao encontrado -- o repo irmao precisa estar ao lado")
    bruto = "".join(
        p.read_text(encoding="utf-8")
        for p in sorted((LIVRO / "chapters").glob("*.tex"))
        + sorted((LIVRO / "backmatter").glob("*.tex"))
    )
    #  ~ e espaco nao-separavel do TeX, nao texto; \ldots{} e -- sao markup.
    bruto = bruto.replace("~", " ").replace("\\ldots{}", "…").replace("--", "—")
    return re.sub(r"\s+", " ", bruto)


def blockquotes(texto: str):
    blocos, atual = [], []
    for linha in texto.splitlines():
        if linha.startswith(">"):
            conteudo = linha[1:].strip()
            if conteudo:
                atual.append(conteudo)
            elif atual:
                blocos.append(" ".join(atual))
                atual = []
        elif atual:
            blocos.append(" ".join(atual))
            atual = []
    if atual:
        blocos.append(" ".join(atual))
    return blocos


def nucleo(bloco: str) -> str:
    t = re.sub(r"\s+", " ", bloco.strip())
    rotulado = re.match(r'^\*\*[^*]+:\*\*\s*"?(.+?)"?$', t)
    return rotulado.group(1) if rotulado else t.strip('"').strip("“”")


def main() -> int:
    src = fonte_do_livro()
    alvos = sys.argv[1:] or ["materiais"]
    arquivos = []
    for alvo in alvos:
        p = pathlib.Path(alvo)
        arquivos += [p] if p.is_file() else sorted(
            f for f in glob.glob(f"{alvo}/**/*.md", recursive=True)
            if not f.endswith("README.md")
        )

    total = falhas = 0
    for md in arquivos:
        for bloco in blockquotes(pathlib.Path(md).read_text(encoding="utf-8")):
            total += 1
            citacao = nucleo(bloco)
            if citacao not in src:
                falhas += 1
                print(f"FALHA {md}\n      {citacao[:100]}")

    print(f"\n{total} citacoes conferidas, {falhas} falha(s)")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
