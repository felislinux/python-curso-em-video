#exercicio 42# Refaça DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
# Exercício Python #042 - Analisando Triângulos v2.0

print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)
r1 = float(input('\033[1;31mPrimeira reta:\033[m '))
r2 = float(input('\033[1;31mSegunda reta:\033[m '))
r3 = float(input('\033[1;31mTerceira reta:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um triângulo ',end='') #junta condições abaixo em uma só linha
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
"""r1 é diferente do r2 | r2 é diferente do r3 | só que não foi testado se o r1 é diferente de r3 
Isso pq se eu tenho uma coisa A que é igual a B, e o B é igual ao C,posso afirmo automaticamente que A é igual C
Igualdade é inclusiva, a "diferença não" , o A pode ser diferente de B, blz, o B pode ser diferente de C, blz
mas o A pode ser igual a C"""
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo.')