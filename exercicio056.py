media=maior=0
nome2=''
mulher20=0
for n in range(1,5):
    print('-'*5,'{}° pessoa'.format(n),'-'*5)
    nome=input(('NOME: '))
    idade=int(input('IDADE: '))
    genero=input('SEXO [M/F]: ').upper()
    media+=idade
    if n==1 and genero=='M':
        maior=idade
        nome2=nome
    elif genero=='M' and maior<idade:
        maior=idade
        nome2=nome
    elif genero=='F' and idade<20:
        mulher20+=1
print('A media de idade do grupo é de  {}.'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior,nome2))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher20))