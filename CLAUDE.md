# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este repositório

**Material de apoio editorial** ao livro infantojuvenil *Maria e o Holossoma — A
Jornada pelos 4 Corpos*, de Maryana Nunes (Editares), cujo repositório é o irmão
`../mary-livro`. O destino dos materiais é a internet.

**Não é software.** Não há testes e não há aplicação para rodar. Os artefatos
são texto editorial em Markdown e os `.docx` e `.pdf` gerados a partir dele por
`materiais/_comum/build.sh` — um script de conversão, não uma aplicação. O
equivalente a "teste" aqui é **fidelidade ao livro** — ver
[Verificação](#verificação).

Tudo é escrito em **português do Brasil**: documentação, conteúdo e mensagens de
commit.

## Estado atual: experimento

As vinte fichas em `ideias/` são **propostas redigidas, ainda não avaliadas e
ainda não aprovadas** pela autora nem pela editora. Nada ali é compromisso de
publicação.

`materiais/` tem **as vinte produzidas**, mais `como-conduzir-os-exercicios/`,
que é transversal. Tudo é MVP — serve para testar conteúdo e fluxo de produção,
**não está aprovado** e não fecha o visual. O índice fica em
`materiais/README.md`; o porquê da ordem em que foram feitas, e o que ficou
pendente, em `docs/prioridades.md`.

Produzir não é aprovar: a etapa atual do projeto continua sendo **avaliar**.
O que mudou é que a avaliação agora acontece sobre material imprimível, e não
sobre descrição. Nenhuma peça foi testada em impressora doméstica ainda.

## A dependência de `../mary-livro`

O livro é a **fonte da verdade** de tudo neste repositório. Antes de propor,
escrever ou revisar qualquer material, leia `docs/o-livro.md`.

Onde conferir um fato no repositório irmão:

| caminho | conteúdo |
|---|---|
| `../mary-livro/chapters/cap01.tex` … `cap06.tex` | **o livro** — são a fonte, editados à mão |
| `../mary-livro/backmatter/` | informações aos pais, atividade de recorte, caixas finais |
| `../mary-livro/config/pauta.tex`, `config/blocos.tex` | parâmetros do diário manuscrito (FR Cursive 13 pt, pauta ciano 25%, passo 19 pt) |
| `../mary-livro/tecnico.md` | por quê de cada decisão técnica do livro |

**Nunca edite `../mary-livro` a partir daqui.** A atualização do livro para
apontar para os materiais é a última etapa do projeto, e só acontece depois de
haver material aprovado.

## Os documentos e seus papéis

| arquivo | responde |
|---|---|
| `README.md` | o que é o repositório, o estado experimental, requisitos de publicação |
| `docs/o-livro.md` | **a obra** — capítulos, glossário com as definições literais, analogias, recursos didáticos, princípios editoriais |
| `ideias/README.md` | as vinte fichas: critério de seleção, as cinco regras comuns, índice e dependências |

Não replique conteúdo entre eles. Fato sobre o livro entra em `docs/o-livro.md`;
fato sobre as fichas entra em `ideias/README.md`.

## As regras que o livro impõe — inegociáveis

Não são preferência de estilo. O livro se fecha com *"Não acredite em nada, nem
mesmo nas informações expostas neste livro. Experimente. Tenha as próprias
experiências."* (`../mary-livro/backmatter/sobre-a-autora.tex`). Material que
apresente os conceitos como fato estabelecido, ou peça adesão em vez de
experimento, contradiz a obra que deveria apoiar.

As cinco regras de `ideias/README.md`, que valem para qualquer material novo:

1. **A pergunta nunca contém a resposta.** "O que você percebeu?", jamais
   "sentiu formigar, né?".
2. **"Não senti nada" é resultado válido** — está escrito em cada ficha em que
   cabe.
3. **Todo material fecha em registro**, escrito ou desenhado, no formato
   objetivo → método → resultados → registros do capítulo *Mão na massa*.
4. **Nenhum material pede para convencer alguém.**
5. **Referência por nome de capítulo, nunca por página** — a paginação não está
   fechada com a gráfica.

Mais três que decorrem da obra e são fáceis de violar sem perceber:

- **A criança propõe a analogia; o adulto só valida.** No livro, a ponte, a
  bateria de celular e o pokémon são invenções da Maria — Antônio responde "Boa
  analogia". Material que explica em vez de perguntar rompe com o recurso
  central da obra. A ficha nº 17 chega a proibir reutilizar as analogias do
  livro.
- **O livro não converte os colegas no final.** O conflito de abertura se
  resolve com a criança praticando tolerância, não com adesão dos outros.
- **A família não é substituída.** Mãe, pai e avó participam dos experimentos
  dentro do próprio livro.

O detalhamento, com citação e arquivo de origem, está em `docs/o-livro.md`
§6 *Princípios editoriais*.

## Estrutura das fichas de `ideias/`

**A numeração é global (01–20), não por pasta.** O número é o ID estável; a
pasta é só metadado de público. Uma ficha pode trocar de diretório na revisão
sem renumerar as outras.

Existem **dois templates rígidos, espelho um do outro**, e um terceiro formato
livre:

| | `crianca-e-mediador/` (01–09) | `crianca-apenas/` (10–17) | `pais-e-educadores/` (18–20) |
|---|---|---|---|
| metadados | Origem · Veículo · Objetivo · Duração · Materiais | idem | Origem · Para · Objetivo · Duração |
| seções | Antes de começar · Passo a passo · Como registrar · **Para o adulto** | Antes de começar · Passo a passo · Como registrar · **Uma coisa importante** (+ *Depois* em 4) | livre, organizado por cenário |

A seção `## Para o adulto` da primeira categoria é substituída por `## Uma coisa
importante` na segunda: a proteção epistêmica que na primeira é entregue ao
adulto, na segunda é entregue diretamente à criança. O "Para o adulto" é sempre
**restritivo** — diz o que *não* fazer; o adulto é operador logístico, nunca
validador de resultado.

**Dependências entre fichas:** a nº 20 é pré-requisito das nº 06, 07, 14 e 15; a
nº 12 depende de umas dez noites já anotadas na nº 11. As demais são de ordem
livre.

### Convenções de formatação das fichas

- **Nenhum frontmatter YAML.** Os metadados são linhas `**Campo:** valor` em
  negrito logo abaixo do H1, sem linha em branco entre elas.
- H1 no formato `# NN · Título`, com **middle dot** (U+00B7), não hífen.
- Seções em H2. **Nenhum H3 nas fichas** (só em `ideias/README.md`, para as três
  categorias).
- Prosa hard-wrapped em **78 colunas**. Tabelas e links podem passar.
- Citação literal do livro em blockquote; nunca inventar fala de Maria ou de
  Antônio.

## `materiais/` — o que foi produzido

Uma pasta por peça, **nomeada só pelo nome, sem o número**: o número da ficha
continua sendo o ID estável e aparece dentro dos documentos, mas é o nome da
pasta que vira URL, e URL com número envelhece mal.

Há **dois tipos de pasta**, e a distinção existe para não duplicar conteúdo:

- **de uma ficha** — `minha-ficha-de-experimento/`, `agua-e-areia/`,
  `conduzir-sem-induzir/`, e assim por diante;
- **transversal** — `como-conduzir-os-exercicios/`, que não sai de nenhuma
  ficha e cobre o que vale para todas: a inversão pedagógica, os cinco tempos
  de uma sessão, a ordem e as dependências, o limite do papel do adulto.

O transversal **remete** ao material de cada ficha em vez de repeti-lo, e
manda para `conduzir-sem-induzir/` tudo que for de bioenergia. Ao acrescentar
conteúdo, decida primeiro em qual dos dois ele cabe.

Três arquivos por peça, todos commitados: `.md` é a fonte da verdade, `.docx`
serve à edição da autora no Word, `.pdf` é o imprimível A4. **`.docx` e `.pdf`
são sobrescritos pelo build sem aviso** — edição feita no `.docx` tem de voltar
para o `.md`, ou se perde.

```sh
./materiais/_comum/build.sh                       # tudo
./materiais/_comum/build.sh materiais/uma-pasta   # só uma
```

Precisa de `pandoc` e `pdflatex`; não precisa de Word nem de LibreOffice.

Nos `.md` das peças imprimíveis, marcadores que o build expande por formato de
saída — `{{linhas:N}}`, `{{moldura:NNmm}}`, `{{pagina}}`, `{{corte}}` e
`{{colunas:N|A|B|C}}`. Existem para o `.md` continuar diffável: sem eles, o
OOXML cru de cada linha pautada moraria dentro do arquivo. A expansão está em
`materiais/_comum/expandir.py`; o racional completo, em `materiais/README.md`.

**Tabela do Markdown não põe fio entre as linhas do corpo.** A de pipe ainda
sai estreita e centrada no PDF; a de *grid* sai em largura cheia, mas as duas
desenham fio só no topo, no cabeçalho e no rodapé. Três casos, três soluções:

| a tabela é | use |
|---|---|
| leitura corrida | tabela em *grid* do Markdown |
| correspondência — a linha é a unidade de sentido | `{{tabela}}` |
| para escrever dentro | `{{colunas}}` |

O caso do meio já quebrou uma peça: no guia da ficha nº 20 os pares "não
pergunte / pergunte" viraram um bloco corrido e se perdia qual linha casava
com qual.

**O MVP não reproduz o visual do livro de propósito.** A pauta ciano de 25% e a
FR Cursive de `../mary-livro/config/pauta.tex` ficaram fora; as linhas saem em
preto a 15%, com passo de 8 mm — o do caderno escolar brasileiro, não os 19 pt
calibrados para a cursiva composta do livro. Ver `materiais/_comum/preambulo.tex`.

## Convenções de escrita

Herdadas de `../mary-livro/CLAUDE.md`:

- Documentação `.md` e conteúdo editorial: **com acentos**, normalmente.
- Mensagens de commit: em português, **sem acentos**, presente do indicativo na
  terceira pessoa — *"Cria"*, *"Reescreve"*, *"Corrige"*.

## Verificação

Não há suíte de testes. O equivalente é fidelidade ao livro, mais a sanidade
dos arquivos que a autora vai abrir. **Rode isto ao alterar conteúdo
editorial:**

```sh
python3 tools/conferir.py       # sai 1 se algo falhar
```

Ele confere as cinco coisas: todo `.md` de peça tem `.docx` e `.pdf` ao lado;
todo PDF está em A4; todo `.docx` é zip válido com XML bem formado; nenhuma
referência por número de página; e toda citação literal existe no fonte de
`../mary-livro` — este último delegado a `tools/conferir-citacoes.py`.

Para achar um trecho no livro e ver o contexto:

```sh
python3 tools/buscar-no-livro.py "trecho procurado"
python3 tools/buscar-no-livro.py -c 300 "trecho"     # mais contexto
```

**Prefira essa busca ao `grep` cru.** O fonte do livro usa espaço inseparável
do LaTeX no meio de frases — `É~importante`, `outros.~Ele` —, e um `grep -F` do
trecho com espaço normal **não acha**, mesmo a citação estando literalmente
certa. Já produziu falso positivo em `materiais/o-que-o-amparador-nao-e/`. O
`buscar-no-livro.py` e o `conferir-citacoes.py` normalizam o `~`; o `grep` na
mão, não.

Contagens declaradas são medidas, nunca escritas à mão:

```sh
grep -c '\\fala{' ../mary-livro/chapters/*.tex
grep -ohE '\\(prancha|pranchaQuebra)\{image' ../mary-livro/chapters/*.tex \
     ../mary-livro/backmatter/*.tex | wc -l
```

**Toda afirmação sobre o livro precisa de arquivo de origem citado.** Quando
este repositório divergir de um `.tex` de `../mary-livro`, o `.tex` vence.
