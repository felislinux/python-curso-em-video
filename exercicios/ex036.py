#exercicio 36#  Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
# ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado
# Exercício Python #036 - Aprovando Empréstimo
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
financiamento = int(input('Quantos anos de financiamento? '))
prestacao = casa / (financiamento * 12)
purcentagem = salario * 30 /100

print('Para pagar uma casa de R$ {} em {} anos a prestação sera de R${:.2f}'.format(casa,financiamento,prestacao))
if prestacao > purcentagem:
    print('Emprestimo NEGADO')
else:
    print('Emprestimo APROVADO')



#print('Emprestimo NEGADO')
#print('Emprestimo APROVADO')