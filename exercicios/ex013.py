#exercicio 13# Faça um prog que leia o salario de um funcionario e mostre um aumento de 15% nele

salario = float(input('Qual seu salario: '))
#10% ou 10 por 100 10*10/100
novo = salario + (salario * 15 / 100)

print('Funcionario que ganhava R${:.2f}, com aumento de 15 %, passara a receber R${:.2f}'.format(salario,novo))
