from datetime import date
dados={}
dados['Nome']=input('Nome: ')
ano=int(input('Ano de Nascimento: '))
idade=date.today().year - ano
dados['Idade']=idade
dados['CTPS']=int(input('Carteira de trabalho (0 não tem ): '))
if dados['CTPS']!=0:
    dados['Contratação']=int(input('Ano de contratação: '))
    dados['Sálario']=float(input(('Sálario: R$')))
print('-=-'*20)
for c,v in dados.items():
   print(f'{c} tem o valor {v}.')
