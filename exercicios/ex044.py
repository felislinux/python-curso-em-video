# exercicio 44# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
#Exercício Python #044 - Gerenciador de Pagamentos

print('{:=^40}'.format('LOJAS GUANABARA'))
preço =float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção: '))

if opção == 1:
    total = preço - (preço *10 /100)
elif opção == 2:
    total = preço - (preço * 5 /100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de  R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/ 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra sea parcelada em {}x de R${:.2f}'.format(totalparc,parcela))
else:
    total = preço
    print('Opçao invalida de pagamento, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço,total))
