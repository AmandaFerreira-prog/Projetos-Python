salario=float(input('Qual o salario do funcionario? R$ '))
aumento=salario*(115/100)
print('Um funcionario que ganhava R${},agora com o aumento de 15% agora ganha R${:.2f}'.format(salario,aumento))