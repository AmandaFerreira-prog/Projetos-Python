print('='*9,'Lojas AMANDIVA','='*9)
preco=float(input('Valor das compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão ')
print('[ 4 ] 3x ou mais no cartão')
opcao=int(input('Qual é a opção? '))
if opcao==1:
    valor=preco*(90/100)
    print('Você ganhou um desconto de 10%!')
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,valor))
elif opcao==2:
    valor=preco*(95/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,valor))
elif opcao==3:
    valor=preco/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(valor))
    print('Sua compra de R${:.2f} não tera acréscimos no final'.format(preco))
elif opcao==4:
    parcela=int(input('Quantas parcelas? '))
    valor2=preco*(120/100)
    valor=valor2/parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela,valor))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,valor2))




