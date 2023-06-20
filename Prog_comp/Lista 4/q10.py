x = int(input('Informe a coordenada inicial de x:'))
y = int(input('Informe a coordenada inicial de y:'))
xaux, yaux = x, y
qnt_mov = 0
qnt_val = 0
while True:
    movimento = str(input('\nInsira para onde o robô deve se deslocar: '))
    movimento = movimento.lower()
    qnt_mov +=1
    if movimento == 'u':
        y += 1
        qnt_val += 1
    elif movimento == 'd':
        y -= 1
        qnt_val += 1
    elif movimento == 'r':
        x += 1
        qnt_val += 1
    elif movimento == 'l':
        x -= 1
        qnt_val += 1
    elif movimento == 'o':
        y += 1
        x -= 1
        qnt_val += 1
    elif movimento == 'n':
        y += 1
        x +=1
        qnt_val += 1
    elif movimento == 'e':
        y -= 1
        x += 1
        qnt_val += 1
    elif movimento == 'w':
        y -= 1
        x -= 1
        qnt_val += 1
    else:
        print('\nInforme uma letra válida!\n: U (cima) - D (baixo) - R (direita) - L (esquerda)')
        print(': O (cima-esquerda) - N (cima-direita) - E (baixo-direita) e W (baixo-esquerda)\n')
    print(f'A posição Inicial foi: {xaux, yaux}\nA posição Final é: {x,y}')
    print(f'Quantidade de Movimentos: {qnt_mov}\nQuantidade de Movimentos Válidos: {qnt_val}')
    if xaux > 0 and yaux > 0:
         print(f'O robô iniciou no primeiro quadrante nas coordenadas: {xaux,yaux}')
    elif xaux < 0 and yaux > 0:
         print(f'O robô iniciou no Segundo quadrante nas coordenadas: {xaux,yaux}')
    elif xaux < 0 and yaux < 0:
         print(f'O robô iniciou no Terceiro quadrante nas coordenadas: {xaux,yaux}')
    elif xaux > 0 and yaux < 0:
         print(f'O robô iniciou no Quarto quadrante nas coordenadas: {xaux,yaux}')
    else:
         print(f'O robô não está definido em um Quadrante nas coordenadas: {xaux,yaux}')
    if x > 0 and y > 0:
         print(f'O robô terminou no primeiro quadrante nas coordenadas: {x,y}')
    elif x < 0 and y < 0:
         print(f'O robô terminou no Terceiro quadrante nas coordenadas: {x,y}')
    elif x < 0 and y > 0:
         print(f'O robô terminou no Segundo quadrante nas coordenadas: {x,y}')
    elif x > 0 and y < 0:
         print(f'O robô terminou no Quarto quadrante nas coordenadas: {x,y}')
    else:
         print(f'O robô não está definido em um Quadrante nas coordenadas: {x,y}')