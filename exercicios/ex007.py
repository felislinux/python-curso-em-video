#exercicio 7# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
media = (nota1 + nota2) / 2
print('A media do aluno é: ',media)
print('A media entre {} e {} é : {:.1f}'.format(nota1,nota2,media)) #.1f só 1 ponto flutuante