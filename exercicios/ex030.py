#exercicio 30# rie um programa que leia um número inteiro e mostre na
# tela se ele é PAR ou ÍMPAR. # Par ou Ímpar?

numero = int(input('Me diga um numero qualquer: '))

if (numero%2) == 0:
        print("O numero digitado foi {} e ele é Par".format(numero))
else:
        print("O numero digitado foi {} e ele é Ímpar".format(numero))