#exercicio 35# Leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#Exercício Python #035 - Analisando Triângulo v1.0

print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)
r1= float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[0;33;41mPODEM FORMAR\033[0;33;41m triangulo')
else:
    print('Os segmentos acima \033[0;33;41m NÃO PODEM FORMAR triangulo\033[0;33;41m')
