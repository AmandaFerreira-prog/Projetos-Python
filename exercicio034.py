salario=float(input('Qual o salario do funcionário? R$ '))
if salario>1250:
    aumento=salario*(110/100)
else:
    aumento=salario*(115/100)
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora.'.format(salario,aumento))