#exercicio 9# Faça um programa que leia um numero inteiro qq e mostre na tela
# a sua tabuada *1 *2 *3 *4 *5 ...
valor = int(input('Entre com um número para saber a tabuada: '))
print('\n De forma feia tudo em uma linha: ')
tabu = valor * 1 , valor * 2 , valor * 3, valor * 4, valor * 5, valor * 6, valor * 7, valor * 8, valor * 9, valor * 10
print('A Tabuada de {} na sequencia é {} : '.format(valor,tabu))
print('\n De forma bunitinha :')#de forma classica e bonita
print('{} x {} = {}'.format(valor,1,valor*1))
print('{} x {} = {}'.format(valor,2,valor*2))
print('{} x {} = {}'.format(valor,3,valor*3))
print('{} x {} = {}'.format(valor,4,valor*4))
print('{} x {} = {}'.format(valor,6,valor*5))
print('{} x {} = {}'.format(valor,6,valor*6))
print('{} x {} = {}'.format(valor,7,valor*7))
print('{} x {} = {}'.format(valor,8,valor*8))
print('{} x {} = {}'.format(valor,9,valor*9))
print('{} x {} = {}'.format(valor,10,valor*10))


