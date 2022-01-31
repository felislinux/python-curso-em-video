frase =  'Curso em Video Python'
##########0123456789...
print(frase)
print(frase[3]) #quarta letra começando a contar em 0, letra s
print(frase[4]) #esta embora 4 é a 5º letra, letra o
print(frase[3:13]) #da quarta letra ate  a 13 (sendo que a 13 não conta)
###########[inicio:fim:sepula]
print(frase[::2]) # frase inteira pulando de 2 em 2

print('oi')
print('Se for uma frase muito grande, tipo blablablabla'  # o que importa
      'blablablablablablablablablablablablablablablabla'  # é não fechar as
      'blablablablablablablablablablablablablablablabla'  # () , ou seja, 
      'blablablablablablablablablablablablablablablabla'  # pule linhas
      'blablablablablablablablablablablablablablablabla') # em frases longas

frase2 = 'Papai Noel Coelhinho'
print(frase2.count('o')) # conta quantas vezes tem o
print(frase2.count('N')) # e é case sensitive
print(frase2.upper().count('N')) # pode-se combinar funções aqui torna
                                 # maiusculo e conta antes era 1 agora 2

# conta a quantidade de espaços
print(len(frase))
print(len(frase2))

# e se usar strip que tira espaços no começo e fim
frase3 = ' Biluteteia '
print(len(frase3))
print(len(frase3.strip()))

#função replace não muda string, só se fazer atri buição
frase4 = 'Teta Tetinha'
print(frase4[0])
# ---->>> frase4[0] = 'J' # vai dar erro, variavel é imutavel <<<---
print(frase4.replace('Teta', 'Ceca')) #só durante o replace mudou
print(frase4)  # a variavel ficou imutavel, replace fica só na execução
#ou seja o replace mudou somente na chamada do replace, só muda se declarar novamente

frase5 =  'Primero Segundo Tercero'
dividido =  frase5.split()
print(dividido) #mostra a frase dividido
print(dividido[2][2]) #pega o dividido 3, 3º palabra  (Tercero e mostra a 2º letra no caso, letra 'r'
                      #lembrando que começa em 0


