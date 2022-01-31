#exercicio 24# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#Verificando as primeiras letras de um texto

cidade = str(input('Digite o nome da cidade: ')).strip() #.strip tira o espaços
print(cidade[:5].upper() == 'SANTO')  # :5 verifica desde o começo , se tem o tamanho total da palavra
                                     # #:5 pois S-0 A-1 N-2 T-3 O-4 5 (finaliza no 5 que não é lido)
