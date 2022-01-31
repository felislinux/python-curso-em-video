#exercicio 32#Faça um programa que leia um ano qualquer e mostre se ele
# é bissexto. # Exercício Python #032 - Ano Bissexto

from time import sleep

#resolvido matematicamente falando
from datetime import date
ano = int(input('Que ano quer analisar? Coloque [0] para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSESTO'.format(ano))
else:
    print('O ano {} Não é BISSESTO'.format(ano))

###usando função pronta
print('Começando de outra forma....')
sleep (2)
from calendar import isleap
# N módulo calendar. Tem uma função chamada isleap,
# que retorna True se o ano for bissexto

anu = int(input('Verificar qual ano? '))
if isleap(anu):
    print('É bissexto')
else:
    print('Não é bissexto')

