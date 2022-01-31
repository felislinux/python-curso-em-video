#exercicoo 17 # Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#Catetos e Hipotenusa

# de forma matematica

co = float(input('Comprimeiro do cateto oposto: '))
ca = float(input('Comprimeiro do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi)) #.2f deminuir pontos flutuantes

#importanto biblioteca

from math import hypot
co = float(input('Comprimeiro do cateto oposto: '))
ca = float(input('Comprimeiro do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))