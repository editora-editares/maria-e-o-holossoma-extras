# Materiais produzidos

Os materiais complementares, prontos para imprimir e para a autora revisar.
Cada pasta é ou uma ficha de [`ideias/`](../ideias/) que virou material, ou
material **transversal**, que não sai de uma ficha e vale para todas.

**Pasta por nome, sem o número.** O número da ficha (01 a 20) continua sendo o
ID estável e aparece dentro dos documentos; o nome da pasta é o que vira URL
quando isto for para a internet, e URL com número envelhece mal.

| pasta | ficha | para quem |
|---|---|---|
| [`como-conduzir-os-exercicios/`](como-conduzir-os-exercicios/) | — | adulto — **transversal**, vale para todas as atividades |
| [`baralho-do-filtro-pessoal/`](baralho-do-filtro-pessoal/) | 01 | criança e adulto — cartas de recortar |
| [`minha-ficha-de-experimento/`](minha-ficha-de-experimento/) | 02 | criança e adulto — é a folha de registro comum a todas as atividades |
| [`agua-e-areia/`](agua-e-areia/) | 03 | criança com adulto presente |
| [`piquenique-dos-cinco-sentidos/`](piquenique-dos-cinco-sentidos/) | 04 | criança com adulto presente, fora de casa |
| [`gratidao-que-vira-acao/`](gratidao-que-vira-acao/) | 05 | criança com adulto por perto |
| [`a-bateria-do-energossoma/`](a-bateria-do-energossoma/) | 06 | criança, 7 dias — **leia a nº 20 antes** |
| [`a-sacudida-do-cachorro/`](a-sacudida-do-cachorro/) | 07 | criança, repetido — **leia a nº 20 antes** |
| [`o-que-muda-e-o-que-fica/`](o-que-muda-e-o-que-fica/) | 08 | criança com adulto por perto |
| [`entrevista-sobre-a-dessoma/`](entrevista-sobre-a-dessoma/) | 09 | criança e adulto — **a mais delicada** |
| [`diario-de-emocoes/`](diario-de-emocoes/) | 10 | criança sozinha, 3 dias |
| [`diario-das-projecoes/`](diario-das-projecoes/) | 11 | criança sozinha, toda manhã |
| [`sonho-ou-projecao/`](sonho-ou-projecao/) | 12 | criança sozinha — **depende do diário acima** |
| [`teste-do-dedo-indicador/`](teste-do-dedo-indicador/) | 13 | criança sozinha, 7 dias |
| [`caca-sensacoes-do-ev/`](caca-sensacoes-do-ev/) | 14 | criança sozinha, 7 dias — **leia a nº 20 antes** |
| [`a-bola-entre-as-maos/`](a-bola-entre-as-maos/) | 15 | criança sozinha, 5 dias — **leia a nº 20 antes** |
| [`caderno-do-ainda-nao-sei/`](caderno-do-ainda-nao-sei/) | 16 | criança sozinha, o ano todo |
| [`album-de-analogias/`](album-de-analogias/) | 17 | criança sozinha, 4 folhas |
| [`meu-filho-falou-disso-na-escola/`](meu-filho-falou-disso-na-escola/) | 18 | adulto |
| [`o-que-o-amparador-nao-e/`](o-que-o-amparador-nao-e/) | 19 | adulto |
| [`conduzir-sem-induzir/`](conduzir-sem-induzir/) | 20 | adulto — **pré-requisito das atividades de bioenergia** |

**As vinte fichas estão produzidas.** Nenhuma está aprovada. O porquê da ordem
em que foram feitas está em [`docs/prioridades.md`](../docs/prioridades.md).

## Dependências entre as pastas

Três pares não podem ser usados fora de ordem:

- **`conduzir-sem-induzir/` antes** de `a-bateria-do-energossoma/`,
  `a-sacudida-do-cachorro/`, `caca-sensacoes-do-ev/` e `a-bola-entre-as-maos/`
  — são as quatro atividades de bioenergia;
- **`diario-das-projecoes/` antes** de `sonho-ou-projecao/`, e com umas dez
  noites já anotadas, senão não há o que classificar;
- **`minha-ficha-de-experimento/`** é a folha de registro que as atividades
  usam quando pedem "anote na sua ficha".

E uma que não é dependência, mas cuidado: **`entrevista-sobre-a-dessoma/` não
deve ser feita se houver luto recente na família.** Está em destaque no guia
daquela pasta.

**O material transversal remete, não repete.** As instruções didáticas cobrem
o que é comum a todos os exercícios — a inversão pedagógica, os cinco tempos
de uma sessão, a ordem e as dependências, o limite do papel do adulto. O que é
de um exercício só fica na pasta dele, e o que é de bioenergia fica em
`conduzir-sem-induzir/`.

## Três arquivos por peça

| extensão | papel |
|---|---|
| `.md` | **a fonte da verdade.** É o que o git revisa e o que se edita |
| `.docx` | para a autora e a editora editarem e comentarem no Word |
| `.pdf` | A4, é o que se imprime |

Os três ficam commitados. `.docx` e `.pdf` são gerados: **o build sobrescreve
os dois sem avisar.** Se a autora editar o `.docx`, a mudança precisa voltar
para o `.md` antes do próximo build, ou se perde. O git não consegue mostrar
diff de `.docx` — é zip binário —, e neste repositório revisão de texto contra
o livro é a única verificação que existe.

## Build

```sh
./materiais/_comum/build.sh                       # tudo
./materiais/_comum/build.sh materiais/uma-pasta   # só uma
```

Precisa de `pandoc` e `pdflatex`. **Não precisa de Word nem de LibreOffice** —
o pandoc escreve `.docx` sozinho.

## Marcadores

Os `.md` das peças imprimíveis usam marcadores que o build expande para o
formato de saída. Existem para o `.md` continuar legível: sem eles, o OOXML cru
de cada linha pautada estaria dentro do arquivo, e a fonte deixaria de servir
para revisar texto.

| marcador | vira |
|---|---|
| `{{linhas:7}}` | 7 linhas para escrever à mão, passo de 8 mm |
| `{{moldura:185mm}}` | um retângulo vazio de 185 mm de altura, para desenhar |
| `{{pagina}}` | quebra de página |
| `{{corte}}` | linha tracejada de "corte aqui" |
| `{{colunas:12\|A\|B\|C}}` | grade **vazia** de 12 linhas com as colunas A, B e C |
| `{{colunas:16\|[75]A\|[25]B}}` | idem, com largura relativa por coluna |
| `{{tabela\|A\|B}} … {{/tabela}}` | grade **com texto**, fio em toda linha |

O `{{tabela}}` é o único marcador de bloco: as linhas entre a abertura e o
`{{/tabela}}` viram células separadas por `|`. Dentro das células, `**negrito**`
funciona — e nada mais.

O `[75]` é **peso relativo**, não milímetro: os pesos são normalizados pela
largura da mancha.

A expansão vive em [`_comum/expandir.py`](_comum/expandir.py), e não dentro do
`build.sh`: com a chegada da grade — cabeçalho, largura relativa, escape de
LaTeX e de XML — o `awk` deixou de caber.

Prosa não usa marcador nenhum.

**Por que a grade não é uma tabela do Markdown.** Tabela de pipe do pandoc sai
estreita e centrada no PDF; tabela em *grid* sai em largura cheia, mas nenhuma
das duas desenha fio em toda linha — e sem fio por linha não há onde a criança
escrever. O marcador emite `tabular` no LaTeX e `<w:tbl>` no OOXML, com fio em
todas as bordas no mesmo preto a 15% das linhas de escrita.

**E tabela de leitura também não, quando a linha importa.** A tabela em *grid*
do pandoc desenha fio só no topo, no cabeçalho e no rodapé — nunca entre as
linhas do corpo. Numa tabela de **correspondência**, do tipo "não pergunte X /
pergunte Y", os pares viram um bloco corrido e o leitor perde qual linha casa
com qual. Foi o que aconteceu no guia da ficha nº 20, e é o motivo de o
`{{tabela}}` existir.

A regra, então: tabela de **leitura corrida** pode ser Markdown; tabela em que
a **linha é a unidade de sentido** usa `{{tabela}}`; tabela para **escrever
dentro** usa `{{colunas}}`.

**Por que o corte.** Peça pequena — cartão de bolso, carta de baralho — em A4
inteiro é desperdício de papel e não cabe no bolso. A folha leva várias cópias
separadas por `{{corte}}`, e a criança recorta.

## Duas convenções que a verificação depende

**Blockquote é citação literal do livro, e nada mais.** Frase sugerida ao
mediador, exemplo inventado ou fala hipotética vão em itálico. É o que permite
conferir toda citação com um `grep -F` contra `../mary-livro`.

**Referência a capítulo pelo nome, nunca por página.** A paginação não está
fechada com a gráfica.
