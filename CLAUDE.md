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
publicação. A próxima etapa do projeto é avaliá-las; só depois vêm a produção
dos materiais, a publicação e a atualização do livro para referenciá-los.

`materiais/` já tem produção: as fichas nº 02, 03, 18, 19 e 20, mais
`como-conduzir-os-exercicios/`, que é transversal. Tudo é MVP — serve para
testar conteúdo e fluxo de produção, não está aprovado e não fecha o visual.
O índice fica em `materiais/README.md`; a ordem de produção, em
`docs/prioridades.md`.

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

Nos `.md` das peças imprimíveis, três marcadores que o build expande por
formato de saída — `{{linhas:N}}`, `{{moldura:NNmm}}` e `{{pagina}}`. Existem
para o `.md` continuar diffável: sem eles, o OOXML cru de cada linha pautada
moraria dentro do arquivo. O racional completo está em `materiais/README.md`.

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

Não há suíte de testes. O que existe são checagens de fidelidade, todas via
`grep`. Rode-as ao alterar conteúdo editorial:

```sh
# Nenhuma referência por número de página (a paginação não está fechada)
grep -rnE '\bp\. ?[0-9]|página [0-9]|pág\.' README.md docs/ ideias/ \
     --include='*.md' materiais/

# Toda citação entre aspas tem de existir no fonte do livro
grep -rF "trecho citado" ../mary-livro/chapters ../mary-livro/backmatter

**Cuidado com o `~` ao conferir citação.** O fonte do livro usa espaço
inseparável do LaTeX no meio de frases — `É~importante`, `outros.~Ele` —, e um
`grep -F` do trecho com espaço normal **não acha**, mesmo a citação estando
literalmente certa. Já produziu falso positivo em
`materiais/o-que-o-amparador-nao-e/`. Ao conferir, troque `~` por espaço nos
dois lados antes de comparar, ou busque um pedaço curto que não atravesse o
til.

# Contagens declaradas são medidas, nunca escritas à mão
grep -c '\\fala{' ../mary-livro/chapters/*.tex
grep -ohE '\\(prancha|pranchaQuebra)\{image' ../mary-livro/chapters/*.tex \
     ../mary-livro/backmatter/*.tex | wc -l
```

**Toda afirmação sobre o livro precisa de arquivo de origem citado.** Quando
este repositório divergir de um `.tex` de `../mary-livro`, o `.tex` vence.
