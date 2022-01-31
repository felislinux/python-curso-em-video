#exercicio 11#  Leia a largura e a altura de uma parede em metros, calcule sua area e
# a quant. de tinta para pinta-la, sendo qe cada litro de tinta, pinta 2m quadrado
larg = float(input('Digite a largura: '))
altu = float(input('Digite a altura: '))
area = larg * altu
print('Sua parede tem a dimensao de {} x {} e sua area é de {}m²'.format(larg,altu,area))
tinta = area / 2
print('Para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))