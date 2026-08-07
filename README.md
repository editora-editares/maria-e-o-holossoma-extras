# Maria e o Holossoma — materiais complementares

Material de apoio ao livro *Maria e o Holossoma — A Jornada pelos 4 Corpos*,
de Maryana Nunes (Editares), cujo repositório é o irmão
[`../mary-livro`](../mary-livro).

O propósito deste repositório é **implementar os materiais complementares e
mantê-los acessíveis pela internet** — o livro impresso hoje não tem nenhum
destino web.

Nada aqui entra no livro impresso. Este repositório não é lido pelo `make` do
repositório do livro, não altera a paginação e não afeta o preflight.

## A relação com o livro, nos dois sentidos

**O livro é a fonte da verdade.** Todo material daqui deriva de algo que a obra
afirma. Antes de propor qualquer coisa, leia [`docs/o-livro.md`](docs/o-livro.md):
é o entendimento consolidado da obra — a história, os conceitos com as analogias
que o próprio livro usa, os recursos didáticos e os princípios editoriais.

**Depois, o livro aponta para cá.** Quando os materiais estiverem prontos e
aprovados, `../mary-livro` será atualizado para referenciá-los. Hoje o único
canal impresso da obra é o e-mail `mariaeoholossoma@gmail.com`, em
`../mary-livro/backmatter/sobre-a-autora.tex`; não existe site nem QR code do
livro — os dois QRs impressos apontam para a editora, não para a obra.

## Estado atual: experimento

As vinte fichas de atividade em [`ideias/`](ideias/) são **propostas redigidas,
ainda não avaliadas e ainda não aprovadas** pela autora nem pela editora. Nada
ali é compromisso de publicação: são um experimento, e a próxima etapa é
justamente avaliá-las.

Treze fichas já viraram material, como MVP — as de nº 02, 03, 04, 08, 11, 12,
13, 14, 15, 16, 18, 19 e 20 —, mais
[`materiais/como-conduzir-os-exercicios/`](materiais/como-conduzir-os-exercicios/),
que não sai de nenhuma ficha e reúne as instruções didáticas comuns a todas.
O índice está em [`materiais/README.md`](materiais/README.md).

Tudo isso existe para testar conteúdo e fluxo de produção, não para fechar o
visual — e nada está aprovado. As outras 7 fichas continuam só como proposta,
e não há site.

## As regras que o livro impõe a qualquer material

Não são preferências de estilo. O livro se fecha com a frase *"Não acredite em
nada, nem mesmo nas informações expostas neste livro. Experimente. Tenha as
próprias experiências."* — material que apresente os conceitos como fato
estabelecido, ou que peça adesão em vez de experimento, contradiz a obra que
deveria apoiar.

As cinco regras já escritas em [`ideias/README.md`](ideias/README.md):

- **A pergunta nunca contém a resposta.** "O que você percebeu?", jamais
  "sentiu formigar, né?".
- **"Não senti nada" é resultado válido** — Maria não sente nada nas primeiras
  tentativas, e o livro diz que isso "é completamente normal".
- **Todo material fecha em registro**, escrito ou desenhado, no formato
  objetivo → método → resultados → registros do capítulo *Mão na massa*.
- **Nenhum material pede para convencer alguém.**
- **Referência por nome de capítulo, nunca por página** — a paginação não está
  fechada com a gráfica.

E o que vem da própria obra, detalhado em
[`docs/o-livro.md` § Princípios editoriais](docs/o-livro.md#6-princípios-editoriais--o-que-um-material-derivado-não-pode-violar):
não induzir crença, não fazer proselitismo, respeitar a autonomia e o ritmo da
criança, não mistificar o amparador, manter as práticas seguras e **não
substituir o papel da família**.

## Como o material é produzido

O `.md` é a fonte; `pandoc` gera o `.docx`, para a autora e a editora editarem
no Word, e o `.pdf` A4, que é o que se imprime. Não é preciso Word nem
LibreOffice para rodar o build. O detalhe está em
[`materiais/README.md`](materiais/README.md).

A tecnologia de **publicação na web** continua em aberto — será decidida na
etapa de produção. O que a solução terá de atender:

- **Papel é o destino dominante.** Boa parte das fichas termina em folha
  preenchida à mão. O entregável mais comum será PDF A4 imprimível em impressora
  doméstica, legível em preto e branco.
- **Leitura em celular**, porque quem lê a ficha é o adulto mediador, com a
  criança ao lado.
- **Nenhuma coleta de dados de criança.** A ficha nº 11 diz explicitamente que
  o diário é da criança e que ela decide se mostra e para quem. Diário
  sincronizado em nuvem contradiz a própria ficha.
- **URL curta e estável**, porque o destino é virar QR code impresso numa edição
  que não se corrige depois de rodar.
- Português do Brasil.

## Convenções

Herdadas de `../mary-livro/CLAUDE.md`:

- Documentação `.md` e conteúdo editorial: **com acentos**, normalmente.
- Mensagens de commit: em português, **sem acentos**, presente do indicativo na
  terceira pessoa — *"Cria"*, *"Reescreve"*, *"Corrige"*.

## Próximas etapas

1. **Avaliar** as vinte ideias de `ideias/`, e o MVP já produzido da nº 02.
2. **Produzir** os materiais aprovados.
3. **Publicar** na internet.
4. **Atualizar `../mary-livro`** para referenciar o que foi publicado.
