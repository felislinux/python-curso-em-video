nome = str(input('Qual o seu nome? '))
if nome == 'Junior': #condição
    print('Que nome lindo voce tem!')
else:
    print('Mas que nome feio {}'.format(nome))
print('Bom dia, {}'.format(nome))

##

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ( n1 + n2 ) / 2
print('A sua média foi {:.1f}'.format(m))
if m >=6.0:                            #condição composta
    print('Sua media fi boa! PARABENS!')
else:
    print('Sua media foi baixa! ESTUDE!')
##ou tudo junto
print('parabens' if m >=6 else 'burro') #condição simplificada
