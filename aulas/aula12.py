nome = str(input('Qual é o seu nome? '))
if nome == 'Junior':
    print('Que nome bonito! ')
#elif pode ser usado quantas vezes quiser | Estrutura condicional aninhada
# Aninhada pq esta em formato de ninho, um dentro o outro | tipo boneca russa
elif nome == 'João' or nome == 'Maria' or nome == 'Jose':
    print('Seu nome é bem comum no Brasil ')
elif nome in 'Ana Jéssica Juliana Lica':
    print('Belo nome feminino')
else:
    print('Nossa que nome bosta. ')
print('Tenha um bom dia, {}'.format(nome))