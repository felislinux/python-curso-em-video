#xercicio 40#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
# Python Exercício #041 - Classificando Atletas

from datetime import date
#importa função que mostra tempo
atual = date.today().year #mostra só o ano
nasc = int(input('Ano de nascimento: '))
idade  = atual - nasc
print('O atleta tem: {} anos.'.format(idade))
if idade <= 9:
    print('Classificalção: MIRIM')
elif idade <= 14: #não precisa verificar se é menor de 9, condição ja satisfeita acima
    print('Classificação: INFANTIL')
elif idade <= 19: #não precisa verificar se é menor de 14, condição ja satisfeita acima
    print('Classificação: JUNIOR')
elif idade <= 25: #não precisa verificar se é menor de 19, condição ja satisfeita acima
    print('Classificação: SÊNIOR')
else:  #obvio s enão se enquadra em nada acima, então é acima de 25
    print('Classificação: MASTER')
