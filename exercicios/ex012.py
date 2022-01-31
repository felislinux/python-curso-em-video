#number 8# Leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Qual o valor do produto: R$ '))
#10% ou 10 por 100 10*10/100
desc = produto * 5/100
newvalor = produto - desc
print('O produto de {}, com desconto de 5 % , que ficou {} '
      'pagando a vista fica {}'.format(produto,desc,newvalor))