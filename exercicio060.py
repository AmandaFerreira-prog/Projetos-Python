n=int(input('''Digite um número para
calcular seu Fatorial: '''))
print('Calculando {}! = '.format(n),end='')
n2=fatorial=n
while n2!=0:
    print('{}'.format(n2),end='')
    print(' X ' if n2>1 else ' = ',end='')
    n2-=1
    if n2>0:
        fatorial*=n2
print('{}'.format(fatorial))