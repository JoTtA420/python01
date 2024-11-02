import random
lista=["pedra", "papel", "tesoura"]
player1=input('Escolha sua opção entre pedra, papel e tesoura: ')
player2=random.choice(lista)
if(player1==player2):
    print('Empate')
elif((player1=='pedra' and player2=='tesoura') or (player1=='papel' and player2=="tesoura" and player2=="papel")):
    print(f'player1 venceu!!!({player1} vence de {player2})')
else:
    print(f'Player2 venceu!!!({player2} vence de {player1}) ')