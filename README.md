# Fila-Banco 
Uma fila de Banco baseada em uma Lista, first in e first out.  

Em um banco, há um único caixa e os atendimentos seguem a ordem de chegada. Contudo, pessoas
idosas (60 anos ou mais) têm prioridade e devem ser atendidas antes. Dado que, em alguns dias, o
número de idosos é muito alto, foram estabelecidas as seguintes regras:
1. As pessoas são atendidas conforme a ordem de chegada.
2. No máximo duas pessoas idosas podem ser atendidas antes (“passar na frente”) de uma pessoa
não idosa.
Por exemplo, considere que cada linha a seguir contém a ordem de chegada (identificador) do
cliente e sua idade.
1 21
2 34
3 67
4 61
5 72
6 54
7 75
Se todos os clientes chegaram antes de iniciar o atendimento, a ordem de atendimento seria:
3, 4, 1, 2, 5, 7, 6.
![Uploading image.png…]()
