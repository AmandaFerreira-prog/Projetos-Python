casa=float(input('Valor da casa: R$ '))
salario=float(input('Salario do comprador: R$ '))
anos=int(input('Quantos anos de financiamento? '))
prestacao=casa/(anos*12)
print('Pra pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(casa,anos,prestacao))
maximo=(30/100)*salario
if prestacao>maximo:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo pode ser CONCEDIDO!')
