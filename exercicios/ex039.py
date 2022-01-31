#exercicio 39# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele
# ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Exercício Python #039 - Alistamento Militar

from datetime import date
#importa função que mostra tempo
atual = date.today().year #mostra só o ano
nasc = int(input('Ano de nascimento: '))
idade  = atual - nasc
print('Quem nasceu em {}  tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Chegou a data de você se alistar')
elif idade < 18:
    saldo = 18 - idade #pra saber quanto falta
    alista = atual + saldo
    print('Não chegou a idade de se alistar, faltam ainda {}, voce vai'
          ' se alistar em {}'.format(saldo,alista))
else:
    saldo = idade - 18 #pra saber quanto faltou
    alista = atual - saldo
    print('Se alista vagavundo, devia ter se alistado há {} anos, voce'
          ' vai deveria ter se alistado em {}'.format(saldo,alista))

