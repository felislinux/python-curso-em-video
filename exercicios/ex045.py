# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
# pedra / papel / tesoura

from random import randint # função que sorteia
from time import sleep #função que da sleep

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0, 2)

perguntar = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura

Digite sua escolha: '''))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POOH!!!\n")

print("-=" * 20)
print("O computador escolheu: {}".format(lista[computador])) #mostrar lista na ordem
print("O jogador escolheu: {}".format(lista[perguntar])) #mostrar lista na ordem
print("-=" * 20)

if computador == 0: #pc jogou pedra
    if perguntar == 0: #jodador pedra
        print("Empate!")
    elif perguntar == 1: #jogador papel
        print("Jogador perdeu")
    elif perguntar == 2:   #jogador tesoura
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1: # pc jogou papel
    if perguntar == 0: #jodador pedra
        print("Computador perdeu")
    elif perguntar == 1:  #jogador papel
        print("Empate!")
    elif perguntar == 2: #jogador tesoura
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2: # pc jogou tesoura
    if perguntar == 0: #jodador pedra
        print("Jogador venceu")
    elif perguntar == 1:  #jogador papel
        print("Computador venceu")
    elif perguntar == 2: #jogador tesoura
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")