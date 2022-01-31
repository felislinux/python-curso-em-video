#exercicio 37# screva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
# Exercício Python #037 - Conversor de Bases Numéricas

num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if  opcao == 1:
    print('{} convertido para binario  é igual a {}'.format(num,bin(num)[2:])) #bin()converte em binario
elif opcao == 2:                                                       #[2:] tirar os 2 primeiros caracteres
    print('{} convertido para octal é igual a {}'.format(num,oct(num)[2:])) #oct() converte em octal
elif opcao == 3:                                                     #[2:] tirar os 2 primeiros caracteres
    print('{} convertido para hexadecimal é igual a {}'.format(num,hex(num)[2:])) #hex() converte em hexadecimal
else:                                                                      #[2:] tirar os 2 primeiros caracteres
    print('Opção invalida')



