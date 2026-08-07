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
| [`minha-ficha-de-experimento/`](minha-ficha-de-experimento/) | 02 | criança e adulto — é a folha de registro comum a todas as atividades |
| [`agua-e-areia/`](agua-e-areia/) | 03 | criança com adulto presente |
| [`meu-filho-falou-disso-na-escola/`](meu-filho-falou-disso-na-escola/) | 18 | adulto |
| [`o-que-o-amparador-nao-e/`](o-que-o-amparador-nao-e/) | 19 | adulto |
| [`conduzir-sem-induzir/`](conduzir-sem-induzir/) | 20 | adulto — **pré-requisito das atividades de bioenergia** |

As outras 15 fichas ainda não foram produzidas — e nem avaliadas. A ordem
sugerida de produção está em [`docs/prioridades.md`](../docs/prioridades.md).

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

Os `.md` das peças imprimíveis usam três marcadores que o `build.sh` expande
para o formato de saída. Existem para o `.md` continuar legível: sem eles, o
OOXML cru de cada linha pautada estaria dentro do arquivo, e a fonte deixaria
de servir para revisar texto.

| marcador | vira |
|---|---|
| `{{linhas:7}}` | 7 linhas para escrever à mão, passo de 8 mm |
| `{{moldura:185mm}}` | um retângulo vazio de 185 mm de altura, para desenhar |
| `{{pagina}}` | quebra de página |

Prosa não usa marcador nenhum — só a ficha em branco e a capa da pasta usam.

## Duas convenções que a verificação depende

**Blockquote é citação literal do livro, e nada mais.** Frase sugerida ao
mediador, exemplo inventado ou fala hipotética vão em itálico. É o que permite
conferir toda citação com um `grep -F` contra `../mary-livro`.

**Referência a capítulo pelo nome, nunca por página.** A paginação não está
fechada com a gráfica.
