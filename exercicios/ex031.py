#exercicio 31# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
# até 200Km e R$0,45 parta viagens mais longas.
# Exercício Python #031 - Custo da Viagem

#forma1
dist = float(input('Qual a distancia da sua viagem em KM: '))
print('Voce vai viajar {} kms'.format(dist))
if dist <=200:
    custo1 = dist  * 0.50
    print('Voce precisa pagar {:.1f} reais'.format(custo1))
else:
    custo2 = dist * 0.45
    print('Voce precisa pagar {:.1f} reais'.format(custo2))

#forma2
custo = dist * 0.50 if dist <=200 else dist * 0.45  #if simplificado , tudo no embalo
print('O preço a pagar pela viagem é de R${}'.format(custo))