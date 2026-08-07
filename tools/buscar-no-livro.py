#!/usr/bin/env python3
"""Busca um trecho no fonte de ../mary-livro e mostra o contexto.

E a "conferencia avulsa" que o CLAUDE.md descreve, feita direito: normaliza o
que e MARCACAO do LaTeX antes de comparar, e por isso acha o trecho mesmo
quando o livro usa espaco inseparavel no meio da frase -- "E~importante",
"outros.~Ele". Um `grep -F` do mesmo trecho com espaco normal nao acha, e ja
produziu falso positivo neste repositorio.

    python3 tools/buscar-no-livro.py "trecho procurado"
    python3 tools/buscar-no-livro.py -c 200 "trecho"     # mais contexto

Sai 1 se nao encontrar.
"""
import argparse
import pathlib
import re
import sys

LIVRO = pathlib.Path(__file__).resolve().parent.parent.parent / "mary-livro"


def carregar():
    if not LIVRO.is_dir():
        sys.exit(f"erro: {LIVRO} nao encontrado -- o repo irmao precisa estar ao lado")
    arquivos = (sorted((LIVRO / "chapters").glob("*.tex"))
                + sorted((LIVRO / "backmatter").glob("*.tex"))
                + sorted((LIVRO / "frontmatter").glob("*.tex")))
    for p in arquivos:
        bruto = p.read_text(encoding="utf-8")
        #  ~ e espaco inseparavel do TeX, nao texto.
        limpo = bruto.replace("~", " ").replace("\\ldots{}", "…").replace("--", "—")
        yield p, re.sub(r"\s+", " ", limpo)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("trecho")
    ap.add_argument("-c", "--contexto", type=int, default=120,
                    help="caracteres de contexto de cada lado (padrao 120)")
    args = ap.parse_args()

    alvo = re.sub(r"\s+", " ", args.trecho.strip())
    achou = 0
    for caminho, texto in carregar():
        for m in re.finditer(re.escape(alvo), texto):
            achou += 1
            ini = max(0, m.start() - args.contexto)
            fim = min(len(texto), m.end() + args.contexto)
            rel = caminho.relative_to(LIVRO.parent)
            print(f"\n=== {rel}")
            print(f"…{texto[ini:m.start()]}", end="")
            print(f"[[{texto[m.start():m.end()]}]]", end="")
            print(f"{texto[m.end():fim]}…")

    if not achou:
        print(f"nao encontrado: {alvo[:80]}")
        return 1
    print(f"\n{achou} ocorrencia(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
