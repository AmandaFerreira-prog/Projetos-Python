numeros=[]
while True:
    n=int(input('Digite um valor: '))
    if n not in numeros:
        lista=numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cod=input('Quer continuar? [S/N] ').upper()
    if cod=='N':
        break
print('-=-'*20)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
