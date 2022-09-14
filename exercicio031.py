dis=float(input('Qual é a distacia da sua viagem? '))
if dis <=200:
    print('Voce esta prestes a começar uma viagem de {:.1f}KM'.format(dis))
    print('E o preço da sua passagem será de R${:.2f}'.format(0.50*dis))
else:
    print('Voce esta prestes a começar uma viagem de {:.1f}KM'.format(dis))
    print('E o preço da sua passagem será de R${:.2f}'.format(0.45*dis))
