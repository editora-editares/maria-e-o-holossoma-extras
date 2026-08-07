#!/usr/bin/env python3
"""Expande os marcadores dos .md para o formato de saida (latex ou openxml).

POR QUE ISTO EXISTE

O .md e a fonte da verdade e precisa continuar LEGIVEL: escreve-se
{{linhas:5}}, nao trinta linhas de OOXML cru. Sem este passo, o XML de cada
linha pautada moraria dentro do arquivo e a fonte deixaria de servir para o
unico teste que este repositorio tem -- revisao de texto contra o livro.

Uso:  expandir.py latex|openxml < entrada.md > saida.md

MARCADORES

    {{linhas:7}}                     7 linhas para escrever a mao
    {{moldura:185mm}}                retangulo vazio, para desenhar
    {{pagina}}                       quebra de pagina
    {{corte}}                        linha tracejada de "corte aqui"
    {{colunas:12|A|B|C}}             grade: 12 linhas, colunas A, B e C
    {{colunas:20|[70]A|[30]B}}       idem, com largura relativa por coluna

O [70] no cabecalho e peso relativo, nao milimetro: os pesos sao normalizados
pela largura da mancha. Sem [n], as colunas saem iguais.
"""
import re
import sys

#  Passo de 8mm: e a pauta do caderno escolar brasileiro, nao os 19pt
#  (6,7mm) do livro -- aqui quem escreve e uma crianca com lapis. Em
#  vigesimos de ponto (unidade do OOXML): 8/25.4*72*20 = 454.
PASSO_MM = 8
PASSO_TW = round(PASSO_MM / 25.4 * 72 * 20)
TOM = "D9D9D9"          # preto a ~15%, seguro em laser monocromatica
TOM_TEX = "black!15"

TABCOLSEP_PT = 3.0
ARRAYRULE_PT = 0.4


def esc_tex(s):
    for de, para in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"),
                     ("$", r"\$"), ("#", r"\#"), ("_", r"\_"),
                     ("{", r"\{"), ("}", r"\}")):
        s = s.replace(de, para)
    return s


def esc_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bloco(fmt, linhas_):
    return ["```{=%s}" % fmt] + linhas_ + ["```"]


# ---------------------------------------------------------------------
#  linhas
# ---------------------------------------------------------------------
def linhas(n, fmt):
    if fmt == "latex":
        return bloco("latex", ["\\linhas{%d}" % n])
    p = ('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="4" w:space="1" '
         'w:color="%s"/></w:pBdr><w:spacing w:line="%d" '
         'w:lineRule="exact" w:before="0" w:after="0"/></w:pPr></w:p>'
         % (TOM, PASSO_TW))
    return bloco("openxml", [p] * n)


# ---------------------------------------------------------------------
#  moldura
# ---------------------------------------------------------------------
def moldura(mm, fmt):
    if fmt == "latex":
        return bloco("latex", ["\\moldura{%dmm}" % mm])
    tw = int(mm * 56.7)          # 1mm = 56,7 vigesimos de ponto
    lados = "".join(
        '<w:%s w:val="single" w:sz="4" w:space="4" w:color="%s"/>' % (l, TOM)
        for l in ("top", "left", "bottom", "right"))
    return bloco("openxml", [
        '<w:p><w:pPr><w:pBdr>%s</w:pBdr>'
        '<w:spacing w:line="%d" w:lineRule="exact"/></w:pPr></w:p>'
        % (lados, tw)])


# ---------------------------------------------------------------------
#  corte
# ---------------------------------------------------------------------
def corte(fmt):
    """Linha tracejada de 'corte aqui', para varias copias numa folha."""
    if fmt == "latex":
        return bloco("latex", ["\\corte"])
    #  Paragrafo vazio com borda inferior tracejada. A altura exata
    #  (400) so afasta o tracejado do conteudo de cima e de baixo.
    return bloco("openxml", [
        '<w:p><w:pPr><w:pBdr><w:bottom w:val="dashed" w:sz="6" w:space="8" '
        'w:color="A6A6A6"/></w:pBdr>'
        '<w:spacing w:line="400" w:lineRule="exact" w:before="200" '
        'w:after="200"/></w:pPr></w:p>'])


# ---------------------------------------------------------------------
#  colunas
# ---------------------------------------------------------------------
def _pesos(cabecalhos):
    titulos, pesos = [], []
    for c in cabecalhos:
        m = re.match(r"^\[(\d+)\](.*)$", c)
        if m:
            pesos.append(float(m.group(1)))
            titulos.append(m.group(2).strip())
        else:
            pesos.append(1.0)
            titulos.append(c.strip())
    soma = sum(pesos)
    return titulos, [p / soma for p in pesos]


def colunas(n_linhas, cabecalhos, fmt):
    titulos, fracoes = _pesos(cabecalhos)
    n = len(titulos)

    if fmt == "latex":
        #  A largura de cada p{} sai da mancha menos o que a propria
        #  tabular consome: um filete por borda vertical (n+1) e dois
        #  tabcolsep por coluna. Sem descontar, a tabela estoura a
        #  margem e o pdflatex avisa Overfull \hbox.
        folga = (n + 1) * ARRAYRULE_PT + 2 * n * TABCOLSEP_PT
        #  RAZAO INTEIRA, e nao decimal: \dimexpr so multiplica por
        #  INTEIRO. Escrito "*0.3333", o TeX le "*0" e cospe ".3333" na
        #  pagina como texto -- as colunas colapsam e o numero aparece
        #  impresso dentro da grade. "*333/1000" e a forma correta.
        spec = "|" + "|".join(
            "p{\\dimexpr(\\linewidth-%.1fpt)*%d/1000\\relax}"
            % (folga, round(f * 1000))
            for f in fracoes) + "|"
        cab = " & ".join("\\textbf{%s}" % esc_tex(t) for t in titulos)
        corpo = ["\\noindent\\begin{tabular}{%s}" % spec,
                 "\\hline",
                 "\\rule{0pt}{5.5mm}%s \\\\ \\hline" % cab]
        vazia = "\\rule{0pt}{%dmm}%s \\\\ \\hline" % (PASSO_MM, " & " * (n - 1))
        corpo += [vazia] * n_linhas
        corpo.append("\\end{tabular}")
        return bloco("latex",
                     ["\\par\\nobreak\\vspace{2mm}",
                      "{\\setlength{\\tabcolsep}{%dpt}\\arrayrulecolor{%s}%%"
                      % (TABCOLSEP_PT, TOM_TEX)]
                     + corpo
                     + ["\\arrayrulecolor{black}}", "\\par\\vspace{2mm}"])

    #  OOXML. Largura em pct*50 (5000 = 100%), layout fixo para o Word
    #  nao redistribuir as colunas ao abrir.
    largura = [max(1, round(f * 5000)) for f in fracoes]
    bordas = "".join(
        '<w:%s w:val="single" w:sz="4" w:color="%s"/>' % (l, TOM)
        for l in ("top", "left", "bottom", "right", "insideH", "insideV"))
    xml = ['<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/>'
           '<w:tblBorders>%s</w:tblBorders>'
           '<w:tblLayout w:type="fixed"/></w:tblPr>' % bordas,
           "<w:tblGrid>%s</w:tblGrid>"
           % "".join('<w:gridCol w:w="%d"/>' % w for w in largura)]
    celulas_cab = "".join(
        '<w:tc><w:tcPr><w:tcW w:w="%d" w:type="pct"/></w:tcPr>'
        '<w:p><w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">'
        '%s</w:t></w:r></w:p></w:tc>' % (w, esc_xml(t))
        for w, t in zip(largura, titulos))
    xml.append("<w:tr>%s</w:tr>" % celulas_cab)
    vazias = "".join(
        '<w:tc><w:tcPr><w:tcW w:w="%d" w:type="pct"/></w:tcPr><w:p/></w:tc>' % w
        for w in largura)
    xml += ['<w:tr><w:trPr><w:trHeight w:val="%d"/></w:trPr>%s</w:tr>'
            % (PASSO_TW, vazias)] * n_linhas
    #  Paragrafo vazio depois da tabela: o Word exige que o corpo nao
    #  termine em <w:tbl>, e duas tabelas seguidas sem ele se fundem.
    xml += ["</w:tbl>", "<w:p/>"]
    return bloco("openxml", xml)


# ---------------------------------------------------------------------
def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("latex", "openxml"):
        sys.exit("uso: expandir.py latex|openxml < entrada.md")
    fmt = sys.argv[1]
    saida = []
    for linha in sys.stdin.read().splitlines():
        t = linha.strip()
        m = re.fullmatch(r"\{\{linhas:(\d+)\}\}", t)
        if m:
            saida += linhas(int(m.group(1)), fmt)
            continue
        m = re.fullmatch(r"\{\{moldura:(\d+)mm\}\}", t)
        if m:
            saida += moldura(int(m.group(1)), fmt)
            continue
        if re.fullmatch(r"\{\{pagina\}\}", t):
            saida += (bloco("latex", ["\\newpage"]) if fmt == "latex"
                      else bloco("openxml",
                                 ['<w:p><w:r><w:br w:type="page"/></w:r></w:p>']))
            continue
        if re.fullmatch(r"\{\{corte\}\}", t):
            saida += corte(fmt)
            continue
        m = re.fullmatch(r"\{\{colunas:(\d+)\|(.+)\}\}", t)
        if m:
            saida += colunas(int(m.group(1)), m.group(2).split("|"), fmt)
            continue
        saida.append(linha)
    print("\n".join(saida))
    return 0


if __name__ == "__main__":
    sys.exit(main())
