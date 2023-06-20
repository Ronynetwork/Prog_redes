qt_elem = int(input('Insira o tamanho da lista:'))
lista = list()
if qt_elem > 0:
    for x in range(0,qt_elem):
        elem = int(input('Insira valores na sua lista, utilize 0 para finalizar:'))
        lista.append(elem)
        if (qt_elem +1):
            for y in lista:
                if elem == lista:
                    lista.remove(y)
                    lista.append(elem)
                    continue
        lista.sort()
        print(lista)
        if elem == 0:
            print(lista)
            break
else: print('Utilize apenas valores positivos')