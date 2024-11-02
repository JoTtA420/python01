import random
def Game(numero):
    player2=random.randint(0,5)
    print(f'Player1: {numero} vs Player2: {player2}')
    if (numero+player2)%2==0:
        return 'PAR - Player1 venceu'
    else:
        return 'Ímpar - Player2 venceu'
print('Jogo - par ou ímpar')
print('Números permitidos - 0, 1, 2, 3, 4 ou 5')
print()
print('------------------------------------')
print()
jogadas=int(input('Quantas vezes deseja jogar? '))
for i in range(jogadas):
    player1=int(input('Insira sua jogada: '))
    print(f'{Game(player1)}')