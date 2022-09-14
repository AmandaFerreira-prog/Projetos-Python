veloz=int(input('Qual a velocidade atual do carro? '))
if veloz>80:
    print('\033[0;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('\033[0;31mVoce deve pagar uma multa de \033[0;33m R$ {:.2f}'.format(7.0*(veloz-80)))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('\033[0;33mTenha um bom dia! Dirija com segurança')