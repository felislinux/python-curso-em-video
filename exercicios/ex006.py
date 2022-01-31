#exercicio 6#  Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada

valor = int(input('Digite um numero: '))
dob =  valor * 2
tri = valor * 3
raiz = valor**(1/2)
raiz2 = pow(valor,(1/2))
print('O dobro deste valor é {} , o triplo é {} e a raiz quadrada {}'.format(dob,tri,raiz))
print('Raiz quadrada mostrada de outra forma: ',raiz2)