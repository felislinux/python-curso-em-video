#exercicio 10# Crie um prog. que leia quanto $$ a pessoa tem e
# mostre quantos dolares ela possa comprar $1=R$ 5,6

real = float(input('Quanto dinheiro voce tem em R$: ' ))
dolar = real / 5.50
print('Com {:.2f} reais valor você pode comprar {:.2f} dolares'.format(real,dolar))