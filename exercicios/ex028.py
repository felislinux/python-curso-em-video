#exercicio 28# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# Jogo de advinhação

print('-=-'*15)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-'*15)
from random import randint #importa a função que gera randomicamente numeros inteiros
from time import sleep #importa o modulo sleep que garante colocar um tempo
num = randint(0,5) #entre 0 e 5
#print(num) #posso mostrar só pra debugar
pensou = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(2)
if pensou == num:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('Perdeu babaca!')
