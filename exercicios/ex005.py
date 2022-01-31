#exercicio 5# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e
# seu antecessor, digitou 7 por exemplo, é pra mostrar 6 e 8
valor = int(input('Digite um valor: '))
ant = valor - 1
dep = valor + 1
print('O anterior é {} e o posterior é {}'.format(ant,dep))
##ou
valor = int(input('Digite um valor: '))
print('Para o valor {} O anterior é {} e o posterior é {}'.format(valor,(valor-1),(valor+1)))