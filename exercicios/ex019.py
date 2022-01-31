#exercicio 19 #   Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# dos alunos e escrevendo na tela o nome do escolhido. #Sorteando um item na lista

# import ramdon inteiro
import  random
n1 = str(input('Primeiro aluno: ')) #str chamar o str não é obrigatorio, ja é por padrão
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3 ,n4]
escolhido = random.choice(lista)
print(' O aluno escolhido foi {}'.format(escolhido))

# import somente o choice de random
from random import  choice
n1 = str(input('Primeiro aluno: ')) #str chamar o str não é obrigatorio, ja é por padrão
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3 ,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))