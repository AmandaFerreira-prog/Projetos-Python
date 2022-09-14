'''tabela=(print('-'*40),print(f'{"Tabela de Preços":^40}'),print('-'*40),print('lápis','.'*25,'R$   1.75'),print('Borracha','.'*22,'R$   2.00'),
        print('Caderno','.'*23,'R$  15.90'),print('Estojo','.'*24,'R$  25.00'),print('Transferidor','.'*18,'R$   4.20'),print('Compasso','.'*22,'R$   9.99'),
        print('Mochila','.'*23,'R$ 120.32'),print('Canetas','.'*23,'R$  22.30'),print('Livro','.'*25,'R$  34.90'),print('-'*40))'''
tabela=('Lapis',1.75,
        'Borracha',2.00,
        'Caderno',15.90,
        'Estojo',25.00,
        'Transferidor',4.20,
        'Compasso',9.99,
        'Mochila',120.32,
        'Canetas',22.30,
        'Livro',34.90)
print('-'*50)
print(f'{"Tabela de preços":^50}')
print('-'*50)
for pos in range(0,len(tabela)):
    if pos%2==0:
        print(f'{tabela[pos]:.<40}',end='')
    else:
        print(f'R${tabela[pos]:<20.2f}')
print('-'*50)