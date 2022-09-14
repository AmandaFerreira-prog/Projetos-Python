print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
total=Mmil=barato=0
n=1
nomebarato=''
while True:
    produto=input('Nome do produto: ')
    preco=float(input('Preço: R$ '))
    c=input('Quer continuar? [S/N]: ').upper()
    total+=preco
    if preco>1000:
        Mmil+=1
    if n==1:
        barato=preco
        nomebarato = produto
    else:
        if preco<barato:
            barato=preco
            nomebarato=produto
    if c=='N':
        break
    n+=1
print(f'O total da compra foi de R${total:.2f}.')
print(f'Temos {Mmil} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}.')




