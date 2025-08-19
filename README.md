Projeto da Matéria de Estrutura de Dados.

Opção 3: Gerenciador de Playlist de Músicas
● Conceito: Simular uma playlist de músicas com funcionalidades como
pular para a próxima/anterior e mover músicas de lugar.
● Requisitos Mínimos:
1. Implementar uma classe Playlist que utiliza uma DLL, onde
cada nó armazena o nome de uma música.
2. Implementar as funções básicas: adicionar_musica(nome),
tocar_proxima() e tocar_anterior().
3. Implementar a função principal: mover_musica(nome,
nova_posicao). Esta função deve encontrar uma música pelo
nome, "desconectá-la" de sua posição atual e "reconectá-la" na
nova posição desejada, ajustando todas as referências prev e next
corretamente.
4. Implementar uma função para exibir a playlist na ordem atual.
5. Implementar uma função inverter_playlist() que inverte a
ordem de todas as músicas de forma eficiente (O(n)).
● Principal Desafio: A manipulação correta dos 4 ponteiros (prev.next,
next.prev, etc.) necessários para remover um nó do meio da lista e
reinseri-lo em outro local sem "quebrar" a sequência
