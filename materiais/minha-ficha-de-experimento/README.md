# Minha ficha de experimento

Material da **ficha nº 02** de [`ideias/`](../../ideias/crianca-e-mediador/02-minha-ficha-de-experimento.md).

É a ficha-chave do conjunto: as de nº 03, 04 e 16 mandam a criança "anotar na
ficha de experimento", e é esta. A nº 20 manda voltar a ela quando a criança
começa a inventar resultados para agradar.

## As quatro peças

| peça | para quem | como usar |
|---|---|---|
| [`ficha-em-branco`](ficha-em-branco.md) | criança | imprimir **frente e verso**, uma cópia por experimento |
| [`exemplo-preenchido`](exemplo-preenchido.md) | criança e adulto | ler junto, uma vez, antes da primeira ficha |
| [`guia-do-mediador`](guia-do-mediador.md) | adulto | ler antes de entregar a primeira ficha |
| [`capa-da-pasta`](capa-da-pasta.md) | criança | uma cópia só, na frente da pasta onde as fichas ficam |

Ordem sugerida: o adulto lê o guia; os dois leem o exemplo; a criança recebe a
ficha em branco e a capa.

Cada peça existe em três arquivos com o mesmo nome: `.md` (a fonte), `.docx`
(para editar no Word) e `.pdf` (para imprimir).

## O exemplo preenchido usa o experimento de bioenergia

E isso é deliberado. O experimento do soma, que seria o mais neutro, não
serve: o livro nunca diz o que a Maria **imaginava** que ia acontecer nele, e
preencher esse campo exigiria inventar uma frase dela. O trecho do
energossoma, no capítulo *Mão na massa*, tem os quatro campos literais e em
primeira pessoa — inclusive a expectativa declarada.

O ganho é maior que a conveniência: é nesse trecho que a Maria anota
*"ainda não sinto nada"* e deixa anotado. A regra de que "não senti nada" é
resultado válido aparece **demonstrada numa ficha preenchida**, em vez de
enunciada num aviso.

O risco é o exemplo virar gabarito de sensação. O guia do mediador trata
disso, e o próprio exemplo registra sensações "bem fraquinhas".

## Impressão

A4, uma folha frente e verso por ficha. As linhas saem em preto a 15%: sai em
qualquer impressora doméstica, inclusive monocromática.

**Não é a pauta do livro.** A pauta ciano de 25% com passo de 19 pt e a
FR Cursive de `../mary-livro/config/pauta.tex` ficaram fora deste MVP de
propósito — aqui o passo é de 8 mm, que é a pauta de caderno escolar
brasileiro e o que a mão de uma criança de nove anos pede. Reproduzir o visual
do livro é decisão da etapa de produção, não desta.

## Regerar

```sh
./materiais/_comum/build.sh materiais/minha-ficha-de-experimento
```
