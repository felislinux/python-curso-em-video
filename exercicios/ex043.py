#exercicio 43 #Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
# Exercício Python #043 - Índice de Massa Corporal

peso = float(input("Informe seu peso em (Kg): "))
altura = float(input("Informe sua altura em (m): "))
imc = peso / (altura*altura) #formular pra calcular o imc

print("Seu IMC é: {:.1f}".format(imc))
if imc < 18.5:
    print("Faixa de peso: Abaixo do peso.")
elif 25 > imc >= 18.5:
    print("Faixa de peso: Peso ideal")
elif 30 > imc >= 25:
    print("Faixa de peso: Sobrepeso")
elif 40 > imc >= 30:
    print("Faixa de peso: Obesidade")
else:
    print("Faixa de peso: Obesidade Mórbida")