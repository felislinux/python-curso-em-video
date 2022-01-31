#exercicio 15 # Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro rodou? '))
kms = float(input('Quantos kms carro rodou? '))
pagar = (dias * 60) + (kms * 0.15)
#
print('Devido a ter rodado {} dias e rodado {} kms, você tera que pagar R$ {:.2f} '.format(dias,kms,pagar))
