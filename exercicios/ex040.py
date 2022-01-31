#exercicio 40# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida: - Abaixo de 5.0: REPROVADO | Entre 5.0 e 6.9: RECUPERAÇÃO | 7.0 ou superior: APROVADO
#Exercício Python #040 - Aquele clássico da Média

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {} , a média do aluno é {}'.format(nota1,nota2,media))
if media >= 7:
    print('O aluno esta Aprovado')
elif media <=5:
    print('O aluno esta Reprovado')
else:
    print('O aluno esta em Recuperação')