#exercicio 16 #Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# quebrando um numero

#importando a biblioteca

from math import trunc
num = float(input('Digite um valor (com import de função): '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,trunc(num)))

# sem importar a biblioteca

num2 = float(input('Digite um valor (sem import de função): '))
print('O valor digitado foi {} e a sua portção inteira é {}'.format(num2,int(num2))) #função interna que é o int() que retorna parte inteira
