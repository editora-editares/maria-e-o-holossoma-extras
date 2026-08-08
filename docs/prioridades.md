# Ordem de produção dos materiais

Prioridade das vinte fichas de [`ideias/`](../ideias/) para virarem material.
Critério: **o que destrava mais coisa, pelo menor custo, sem passar na frente
de um requisito de segurança editorial.**

Nada aqui é compromisso — as fichas continuam não avaliadas e não aprovadas.

## As duas dependências que governam a ordem

**Editorial.** A ficha nº 20 é pré-requisito declarado das nº 06, 07, 14 e 15.
Nenhum material de bioenergia deve ser publicado antes dela.

**Técnica.** Seis fichas (06, 07, 08, 12, 15, 16) precisam de **grade ou
colunas impressas**. Tabela de pipe do pandoc sai estreita e centrada; a de
grid sai em largura cheia e resolve o caso de duas colunas de texto, mas nenhuma
das duas dá lugar para escrever. **Resolvido:** o marcador `{{colunas:N|A|B}}`
gera a grade com fio em toda linha, nos dois formatos de saída, com largura
relativa por coluna.

Duas fichas (13, 01) precisam de **formato de cartão**, não A4. **Resolvido**
também: o marcador `{{corte}}` desenha a linha tracejada de "corte aqui", e a
folha A4 leva várias cópias da peça pequena. A nº 01 ainda vai precisar de
cartas maiores, mas o mecanismo já existe.

## Ordem

| # | ficha | situação | por quê |
|---|---|---|---|
| — | *Como conduzir os exercícios* (transversal) | **feita** | instruções didáticas comuns às vinte; não sai de ficha nenhuma |
| — | 02 · Minha ficha de experimento | **feita** | folha de registro comum a todas as outras |
| 1 | 20 · Conduzir sem induzir | **feita** | destrava 4 fichas; é o documento de segurança do repo |
| 2 | 03 · Água e areia | **feita** | primeiro consumidor real da ficha 02 — testa o MVP em uso |
| 3 | 19 · O que o amparador não é | **feita** | a 18 termina apontando para ela |
| 4 | 18 · Meu filho falou disso na escola | **feita** | fecha o kit do adulto |
| 5 | 16 · Caderno do "ainda não sei" | **feita** | encena a última página do livro; estreou a grade de 3 colunas |
| 6 | 08 · O que muda e o que fica | **feita** | reusou a grade (2 colunas) |
| 7 | 04 · Piquenique dos cinco sentidos | **feita** | folha em 5 partes |
| 8 | 11 · Diário das Projeções | **feita** | abre o bloco psicossoma; a 12 e a 13 dependem dele |
| 9 | 12 · Sonho ou projeção? | **feita** | inútil sem umas dez noites da nº 11 |
| 10 | 13 · Teste do dedo indicador | **feita** | estreou o corte, para o cartão de bolso |
| 11 | 15 · A bola entre as mãos | **feita** | melhor lição de método do conjunto (grupo de controle) |
| 12 | 14 · Caça-sensações do EV | **feita** | uma moldura por dia, desenhada pela criança |
| 13 | 07 · A sacudida do cachorro | **feita** | autorregulação **com** verificação |
| 14 | 06 · A bateria do energossoma | **feita** | 7 dias × 3 vezes: maior chance de abandono |
| 15 | 10 · Diário de Emoções | **feita** | independente, mas nada destrava |
| 16 | 17 · Álbum de analogias | **feita** | quatro folhas simples |
| 17 | 05 · Gratidão que vira ação | **feita** | quase só prosa + ficha 02 |
| 18 | 09 · Entrevista sobre a dessoma | **feita** | a mais difícil de conduzir; feita com o kit do adulto já validado |
| 19 | 01 · Baralho do Filtro Pessoal | **feita** | única que precisa de recorte; reusou o corte da nº 13 |

**As vinte estão produzidas.** A lista acima passa a ser registro de por que a
ordem foi essa, não fila de trabalho.

## O que ficou pendente

**Em 12, 18, 19 e 20 o "material" é quase a ficha reimpressa.** A tabela de
critérios da nº 12 já estava escrita dentro dela. Vale decidir se essas quatro
viram PDF ou se são só conteúdo de site — a decisão não foi tomada, elas saíram
nos três formatos como todas as outras.

**As cartas da nº 01 são tiras, não retângulos de baralho.** O `{{corte}}` só
faz corte horizontal, então saem quatro cartas largas por A4. Funciona para
escrever e virar; corte vertical daria o formato esperado.

**Nenhuma peça foi testada em impressora doméstica.** É o único teste que o
repositório não consegue fazer sozinho: imprimir em P&B e conferir se as linhas
a 15% e os fios da grade aparecem e dão para escrever em cima.

**Nada está aprovado.** As vinte fichas continuam sendo propostas não avaliadas
pela autora nem pela editora; agora existem em versão imprimível para que a
avaliação possa acontecer sobre material, e não sobre descrição.
