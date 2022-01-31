#exercicio 25# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# Procurando uma string dentro de outra

#  in é operador do python
nome = str(input('Digite seu nome completo: ')).strip() #.strip tira o espaços
print('Seu nome tem Silva? {}'.format('Silva' in nome)) # procura parala in variavel #spo que só procura 'Silva' do jeito escrito
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper())) #procura SILVA  forçando em maisuculo
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) #procura silva  forçando em minusculo


