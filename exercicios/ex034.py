#exercicio 34# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#P/ salários superiores a R$1250,00, calcule um aumento de 10%. P/ os inferiores ou iguais, o aumento é de 15%.
#Exercício Python #034 - Aumentos múltiplos


# duas vezes print
salario = float(input('Qual é o salario do funcionario ? R$ ' ))
if salario > 1250:
    novo10 = salario + (salario * 10 / 100)
    print('Quem ganhava R$ {} passa a ganhar R$ {} agora'.format(salario, novo10))
else:
    novo15 = salario + (salario * 15 / 100)
    print('Quem ganhava R$ {} passa a ganhar R$ {} agora'.format(salario, novo15))

### ou sendo mais limpo

salario1 = float(input('Qual é o salario do funcionario ? R$ ' ))
if salario1 <= 1250:
    novo = salario1 + (salario1 * 15 / 100)
else:
    novo = salario1 + (salario1 * 10 / 100)
    print('Quem ganhava R$ {} passa a ganhar R$ {} agora'.format(salario, novo))