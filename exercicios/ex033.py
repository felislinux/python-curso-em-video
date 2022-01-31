#exercicio 33# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#Exercício Python #033 - Maior e menor valores

a1 = int(input('Primeiro valor 1: '))
b1 = int(input('Segundo valor 1: '))
c1 = int(input('Terceiro valor 1: '))
# tradicionalmente fazemos assim
if a1 < b1 and a1 < c1:
    menor1 = a1
if b1 < a1 and b1 < c1:
    menor1 = b1
if c1 < a1 and c1 < b1:
    menor1 = c1
#veirifcando quem é o maior
if a1 > b1 and a1 > c1:
    maior1 = a1
if b1 > a1 and b1 > c1:
    maior1 = b1
if c1 > a1 and c1 > b1:
    maior1 = c1

print('O menor valor 1 digitado foi {}'.format(menor1))
print('O maior valor 1 digitado foi {}'.format(maior1))

##
#######
##

#verificando quem é o menor com outro metodo
# ja deduzindo que um dos nuemros é menor
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior  = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
