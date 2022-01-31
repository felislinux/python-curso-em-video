#exercicio 026 # Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# Primeira e última ocorrência de uma string

frase = str(input('Digite uma frase: ')).upper().strip() #joga tudo em misuculo e tira os espaços iniciais ou finais
# mais facil fazer em etapas
print('A leta A aparece {} vezes na frase'.format(frase.count('A'))) #quantas vezes letra A
print('A primeira letra A apareceu na posição {}'.format(frase.find('A'))) #.find procura a primeira vez de algo, mostrando começando em 0
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #.find mesmo acima mas com incremento pra melhorar leitura da posição
#
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A'))) #.rfind procura a ultima vez de algo, independente do tamanho, procura decrescivamente
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #.rfind mesmo acima mas com incremento pra melhorar leitura da posição

