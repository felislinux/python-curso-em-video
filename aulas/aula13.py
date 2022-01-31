print('Oi')
print('Oi')
print('Oi')
print('-------------')
#normalmente
for c in range (0,6):
    print('Ui')
print('Fim') #fim dentro da identação
####
for c in range(1,6): #vai de contar de 1 ate 5
    print(c)
print('vai de contar de 1 ate 5')
###
for c in range(6, 0, -1): #faz agora a contagem recursivamente , decrementando 1
    print(c)
print('faz agora a contagem recursivamente , decrementando 1')
###
for c in range(0, 7, 2): #faz do 0 ate o 6 pulando de 2 em 2
    print(c)
print('faz do 0 ate o 6 pulando de 2 em 2')
#
n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
print('vai mostrar ate o numero digitado: ')
#
n = int(input('Digite um numero: '))
for c in range(0, n+1): #acrescenta +1 a contagem
    print(c)
print('vai mostrar ate o numero digitado +1: ')
##
i = int(input('numero inicial: '))
f = int(input('numero final: '))
p = int(input('quantidade de passos: '))
for c in range (i, f+1, p):
    print(c)
print('você deu todas as etapas do for')
###
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('leu só 1 vez, mas o comando esta dentro do for, ou seja, vai repetir \n3 vezes, de acordo com o anunciado')

#
s = 0
for c in range(0, 4):
    n =int(input('digite um valor: '))
    s = s + n # ou como s += n
print('o somatorio de todos valores foi {} :'.format(s))
#
s = 0
for c in range(0, 4):
    n =int(input('digite um valor: '))
    s += n # ou s = s + n
print('o somatorio de todos valores foi {} :'.format(s))
