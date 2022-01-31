#exercicio 29#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
# multado. A multa vai custar R$7,00 por cada Km
#Radar eletrônico

veloc = float(input('Qual é a velocidade atual do carro? '))
if veloc <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (veloc - 80 )* 7
    print('MULTADO! Você excedeu o limite permitido que é de 60km/h'
          '\nVocê deve pagar uma multa de {}'.format(multa))
