#!/usr/bin/env bash
# =====================================================================
#  materiais/_comum/build.sh  --  Markdown -> .docx + .pdf
# =====================================================================
#  O .md e a fonte da verdade; .docx e .pdf sao gerados e ficam
#  commitados ao lado dele. O .docx existe para a autora e a editora
#  editarem no Word; o .pdf e o que se imprime.
#
#  SE A AUTORA EDITAR O .docx, a mudanca tem de voltar para o .md
#  antes do proximo build -- senao este script a apaga. O git so
#  consegue revisar o .md; .docx e zip binario e nao tem diff.
#
#  Uso:  ./materiais/_comum/build.sh [pasta ...]
#        sem argumento, processa todas as pastas de materiais/
# ---------------------------------------------------------------------
set -euo pipefail

# ---------------------------------------------------------------------
#  Saida determinista
# ---------------------------------------------------------------------
#  Sem isto, pdflatex e pandoc carimbam a hora corrente dentro do .pdf
#  e do .docx. O conteudo sai identico, mas os BYTES nao -- e como os
#  gerados sao commitados, cada build sujava os 22 arquivos de uma vez
#  com ruido puro, enchendo o historico de blob binario que so difere
#  no relogio.
#
#  Data FIXA, e nao a do ultimo commit: com a do commit, o proximo
#  build depois de commitar ja daria bytes diferentes de novo, que e
#  exatamente o problema que se quer evitar.
#
#  2026-01-01 00:00:00 UTC. O valor nao significa nada -- so precisa
#  nao mudar.
export SOURCE_DATE_EPOCH=1767225600
export FORCE_SOURCE_DATE=1

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
COMUM="$RAIZ/materiais/_comum"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

command -v pandoc   >/dev/null || { echo "erro: pandoc nao encontrado"; exit 1; }
command -v pdflatex >/dev/null || { echo "erro: pdflatex nao encontrado"; exit 1; }

# ---------------------------------------------------------------------
#  Expansao dos marcadores
# ---------------------------------------------------------------------
#  O .md fica LEGIVEL: escreve-se {{linhas:5}}, nao trinta linhas de
#  XML. Este passo troca o marcador pelo bloco raw do formato de saida
#  -- LaTeX chama \linhas do preambulo, OOXML emite paragrafos com
#  borda inferior ou uma <w:tbl>.
#
#  Sem isto, a alternativa seria enfiar o OOXML cru dentro do .md, o
#  que destruiria a razao de o .md ser a fonte: revisao de texto
#  editorial legivel no diff.
#
#  A logica esta em expandir.py, e nao aqui: com a chegada do marcador
#  de colunas (grade com cabecalho, largura relativa e escape de LaTeX
#  e de XML) o awk deixou de caber. Rode `expandir.py --help` para a
#  lista de marcadores.
command -v python3 >/dev/null || { echo "erro: python3 nao encontrado"; exit 1; }

expande() {
  python3 "$COMUM/expandir.py" "$1"
}

processa() {
  local md="$1" base nome
  base="$(dirname "$md")"
  nome="$(basename "$md" .md)"
  [ "$nome" = "README" ] && return 0

  expande latex  < "$md" > "$TMP/$nome.latex.md"
  expande openxml < "$md" > "$TMP/$nome.docx.md"

  pandoc "$TMP/$nome.latex.md" -o "$base/$nome.pdf" \
      --pdf-engine=pdflatex -H "$COMUM/preambulo.tex" -V fontsize=11pt \
      -V lang=pt-BR --quiet
  pandoc "$TMP/$nome.docx.md" -o "$base/$nome.docx" \
      -V lang=pt-BR --quiet

  echo "  $nome.pdf  $nome.docx"
}

alvos=("$@")
if [ ${#alvos[@]} -eq 0 ]; then
  mapfile -t alvos < <(find "$RAIZ/materiais" -mindepth 1 -maxdepth 1 -type d ! -name '_*')
fi

for dir in "${alvos[@]}"; do
  echo "$(basename "$dir")/"
  while IFS= read -r md; do processa "$md"; done \
    < <(find "$dir" -maxdepth 1 -name '*.md' | sort)
done
