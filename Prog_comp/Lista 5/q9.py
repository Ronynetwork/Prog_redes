variável = 'Ronyldo'
inv = len(variável)
for x in range((len(variável) +1) * 2):
    if x < len(variável):
        print(variável[:x])
    elif x > len (variável):
        print(variável[:inv])    
        inv -= 1