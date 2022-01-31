#exercicio 22 # rie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas.
"""# - Quantas letras ao todo sem considerar espaços Quantas letras tem o primeiro nome
#Analisador de Textos"""

nome = str(input('Digite seu nome completo: ')).strip() #.strip pode cortar os espaços
print('Analisando seu nome ....')
print('Seu nome em maisuculo é: {}'.format(nome.upper()))
print('Seu nome em minusculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # - nome.count(' ') esta excluindo da contagem algo solicitado
                                                                    # vai remover espaços ' ', se fosse '   ' remove mais espaços, ou  '-' removeria traços
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count('-'))) # por exemplo aqui vai remover caso tenha colocado - entre os nomes
print('Seu nome em primeiro nome tem {} letras '.format(nome.find(' '))) #artificio que começa a contar apos encontrar o primeiro espaço, significa
                                                                         # nome: 'ana maria' por exemplo, quando finaliza ana, tem espaço ai conta ate ele, no caso 3

#de outra forma
nome2 = str(input('Digite nome e sobrenome: '))
separa = nome2.split()
print(separa) #mostra individuais, todos
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))  # separa[0] devido usar função .split separa[numero]
                                                                          # vai mostrar somente o solicitado de acordo com a ordem de separação