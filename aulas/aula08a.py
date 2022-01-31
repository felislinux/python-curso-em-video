from math import sqrt,ceil,floor #importa somente os selecionados
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('a raiz de um número {} é igual a {}'.format(num,ceil(raiz))) #arredonda pra cima
print('e a raiz de um número {} é igual a {}'.format(num,floor(raiz))) #arredonda pra baixo
print('e a raiz de um número {} é igual a {:.2f}'.format(num,raiz)) #formatado diferente


### bibliote que gera um numeros randomicamente
import random
num = random.randint(10,50)
print('o numero gerado foi',num)


#bibliotecas que gera emojis |pacote externo pelo pypi
import emoji
print(emoji.emojize('Quinta série ta chegando :point_right::ok_hand::shit:', use_aliases=True))




