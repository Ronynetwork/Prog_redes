def area(larg, comp):
    print('='*100)
    area_total = larg*comp
    print(f'A área de seu terreno de {larg}x{comp} é de {area_total}')
    print('='*100)
print('='*100)
larg = float(input('Insira a largura de seu terreno: '));print()
comp = float(input('Insira o comprimento de seu terreno: '))
area(larg,comp)