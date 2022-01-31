#exercicio 27#  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Primeiro e último nome de uma pessoa

n = str(input('Digite seu nome completo: ')).strip()
#forma 1 colocando ja dentro o slip e solicitando entrada 0
print('Seu primeiro nome é {}'.format(n.split()[0]))
#mais chique (ou correto) é ja dando a instrução para dividir
nome = n.split()  #ja divide
print(nome)   #imprime dividido
#
print('Muito prazer em conhecer !')
print('Seu primeiro nome é {}'.format(nome[0])) #pq posição 0 sempre é a posição inicial
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) #len() vai ler a quantidade de posições, o -1 vai instruir a mostrar a ultima posição
print('Só pra provar o que foi usado acima o nome tem {} posições'.format(len(nome)))
