print('\033[31mOla mundo')    #vide codigos ansi
print('\033[31;43mOla mundo')
print('\033[1;31;43mOla mundo\033[m') ## \033[m finaliza a personalização
print('\033[4;30;46mOla mundo\033[m')

###
a = 3
b = 5
print('\n Os valores são \033[32m{}\33[m e \033[31m{}\33[m podis crer'.format(a,b))
print('\n Os valores são \033[7;31;43m{}\33[m e \033[7;32;43m{}\33[m podis crer'.format(a,b))

#ou pode ser uando os formats, iniciando e finalizando
nome = 'Junior'
print('\nOla e ai gatão {}{}{} garaaaai'.format('\33[4;34m',nome,'\33[m'))  #começo e finalizo a formatação


#tecnica mais usada no final do curso, no futuro , entendera melhor
nome1 = 'burucutu'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\33[33m',
         'pretoebranco':'\33[7;30m'}
#criado um dicionario
print('Olaaaaaa tudo bemmm, {}{}{}'.format(cores['amarelo'], nome1 ,cores['limpa']))
