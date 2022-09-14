for n in range (1,6):
    peso=float(input('Peso da {}° pessoa: '.format(n)))
    if n==1:
        maior=menor=peso
    if n==2:
        if peso>maior:
            maior=peso
        elif peso<menor:
            menor=peso
    n+=1
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))