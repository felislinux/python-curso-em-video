#exercicio 23# Faça um programa que leia um número de 0 a 9999 e mostre na
# tela cada um dos dígitos separados. # Separando dígitos de um número


### dessa forma funciona, mas tem problema que sempre tem que ser colocado
# um numero com 4 digitos ou havera erro

"""num = int(input('Informe um número: '))
n = str(num)
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('MIlhar: {}'.format(n[0]))"""

###tem outra forma de fazer, matematicamente falando

num2 = int(input('Informe um número: '))
print('Analisando o numero {}'.format(num2))
# pegando a unidade
u = num2 // 1 %10 #divisão por inteiro, dividindo por ele mesmo, tirando modulo de 10
              #pega este numero divido por 10 e pego o resto da divisão, este resto
              # é o que sobrou, que é a unidade
#pra pegar dezena
d = num2 // 10 % 10
#pra pegar centena
c = num2 // 100 % 10
#pra pegar milhar
m = num2 // 1000 % 10

#

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('MIlhar: {}'.format(m))

###video pra entender estes calculos
# https://www.youtube.com/watch?v=uxsh-s4OgLE unidade,dezena, centena, milhar
# https://www.youtube.com/watch?v=qpvJQnrJXxM  divisão de numeros intieros por 10

