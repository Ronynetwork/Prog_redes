n = int(input('Insira um valor inteiro:'))
b = n
c = 1
d = n
if n !=0:
    while n > 1:
        n -= 1
        c = b*(n)
        b = c
    print (f'{d}!=',c)
else:
    print('0!=1')