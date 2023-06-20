val_int = int(input('Informe um valor inteiro para verificar seu fatorial: '))
aux = val_int
var = 1
fatorial = val_int
if val_int !=0:
    for x in range(1,val_int):
        val_int -= 1
        var = aux*val_int
        aux = var
    print (f'[{fatorial}] != ',var)
else:
    print('O número informado é 0, portando, fatorial = 1')