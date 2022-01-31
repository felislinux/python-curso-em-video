#exercicio 20 # O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada. # Sorteando uma ordem na lista

# import ramdon inteiro
import  random
n1 = str(input('Primeiro aluno: ')) #str chamar o str não é obrigatorio, ja é por padrão
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3 ,n4]
random.shuffle(lista)
print('As apresentações setão na seguinte sequencia: ')
print(lista)

# importando somente o metodo suffler
from  random import shuffle
n1 = str(input('Primeiro aluno: ')) #str chamar o str não é obrigatorio, ja é por padrão
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3 ,n4]
shuffle(lista)
print('As apresentações setão na seguinte sequencia: ')
print(lista)