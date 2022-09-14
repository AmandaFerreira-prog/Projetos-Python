dias=int(input('Quantos dias alugados: '))
Km=float(input('Quantos KM percorridos: '))
preco=(60*dias)+(Km*0.15)
print('O total a pagar é de R${:.2f}'.format(preco))
