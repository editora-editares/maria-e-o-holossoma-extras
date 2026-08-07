#!/usr/bin/env python3
"""Verificacao completa dos materiais gerados.

Este repositorio nao tem suite de testes -- o equivalente e fidelidade ao
livro, mais a sanidade dos arquivos que a autora vai abrir. Isto reune as duas
coisas num comando so.

    python3 tools/conferir.py          # sai 1 se algo falhar

O QUE CONFERE

  1. todo .md de peca tem o .docx e o .pdf ao lado
  2. todo .pdf esta em A4 e reporta quantas paginas tem
  3. todo .docx e zip valido com word/document.xml bem formado
  4. nenhuma referencia por numero de pagina (a paginacao do livro nao
     esta fechada com a grafica)
  5. toda citacao literal existe no fonte de ../mary-livro
     -- delegado a tools/conferir-citacoes.py, que tem a logica

O item 5 depende da convencao registrada em materiais/README.md:
BLOCKQUOTE E CITACAO LITERAL DO LIVRO, E NADA MAIS.
"""
import glob
import os
import pathlib
import re
import subprocess
import sys
import zipfile
import xml.dom.minidom

RAIZ = pathlib.Path(__file__).resolve().parent.parent
MATERIAIS = RAIZ / "materiais"

#  595 x 842 pt = A4 retrato. O pdfinfo arredonda, entao comparamos
#  com folga de 1pt.
A4 = (595.276, 841.89)


def pecas():
    for md in sorted(glob.glob(str(MATERIAIS / "*" / "*.md"))):
        if os.path.basename(md) != "README.md":
            yield pathlib.Path(md)


def conferir_trio(falhas):
    for md in pecas():
        for ext in (".docx", ".pdf"):
            if not md.with_suffix(ext).exists():
                falhas.append(f"faltando: {md.with_suffix(ext).relative_to(RAIZ)}")


def conferir_pdfs(falhas):
    print("  paginas")
    for md in pecas():
        pdf = md.with_suffix(".pdf")
        if not pdf.exists():
            continue
        saida = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                               text=True).stdout
        pags = re.search(r"Pages:\s+(\d+)", saida)
        tam = re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", saida)
        nome = str(pdf.relative_to(MATERIAIS))
        print(f"    {nome:<54} {pags.group(1) if pags else '?'} pag")
        if tam:
            l, a = float(tam.group(1)), float(tam.group(2))
            if abs(l - A4[0]) > 1 or abs(a - A4[1]) > 1:
                falhas.append(f"nao e A4: {nome} ({l} x {a})")


def conferir_docx(falhas):
    n = 0
    for md in pecas():
        docx = md.with_suffix(".docx")
        if not docx.exists():
            continue
        try:
            with zipfile.ZipFile(docx) as z:
                if z.testzip() is not None:
                    raise ValueError("zip corrompido")
                xml.dom.minidom.parseString(z.read("word/document.xml"))
            n += 1
        except Exception as e:                              # noqa: BLE001
            falhas.append(f"docx invalido: {docx.relative_to(RAIZ)} -- {e}")
    print(f"  {n} docx validos (zip + XML bem formado)")


def conferir_paginacao(falhas):
    padrao = re.compile(r"\bp\. ?[0-9]|página [0-9]|pág\.")
    alvos = ["README.md"]
    for d in ("docs", "ideias", "materiais", "tools"):
        alvos += glob.glob(str(RAIZ / d / "**" / "*.md"), recursive=True)
    achou = 0
    for caminho in alvos:
        p = RAIZ / caminho if not os.path.isabs(caminho) else pathlib.Path(caminho)
        if not p.is_file():
            continue
        for i, linha in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if padrao.search(linha):
                falhas.append(f"referencia por pagina: {p.relative_to(RAIZ)}:{i}")
                achou += 1
    if not achou:
        print("  nenhuma referencia por numero de pagina")


def conferir_citacoes(falhas):
    r = subprocess.run([sys.executable, str(RAIZ / "tools" / "conferir-citacoes.py")],
                       capture_output=True, text=True, cwd=RAIZ)
    for linha in r.stdout.strip().splitlines():
        if linha.strip():
            print(f"  {linha.strip()}")
    if r.returncode != 0:
        falhas.append("citacoes: ver acima")


def main():
    falhas = []
    print("materiais")
    conferir_trio(falhas)
    conferir_pdfs(falhas)
    print("integridade")
    conferir_docx(falhas)
    conferir_paginacao(falhas)
    print("fidelidade ao livro")
    conferir_citacoes(falhas)

    print()
    if falhas:
        for f in falhas:
            print(f"FALHA  {f}")
        print(f"\n{len(falhas)} falha(s)")
        return 1
    print("tudo certo")
    return 0


if __name__ == "__main__":
    sys.exit(main())
