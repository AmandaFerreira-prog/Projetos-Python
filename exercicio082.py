lista=[]
par=[]
impar=[]
while True:
    n=int(input('Digite um valor: '))
    lista.append(n)
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    op=input('Quer continuar? [S/N] ').upper()
    if op == 'N':
        break
print('-=-'*25)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
