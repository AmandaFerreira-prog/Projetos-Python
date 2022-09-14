dados={}
dados['Nome']=input('Nome: ')
dados['Média']=float(input(f'Média de {dados["Nome"]}: '))
if dados['Média']>=7:
    dados['Situação']='Aprovado'
elif dados['Média']<7 and dados['Média']>5:
    dados['Situação']='Recuperação'
else:
    dados['Situação'] = 'Reprovado'
print('-=-'*30)
#print(f'O nome é igual a {dados["Nome"]} ')
#print(f'Média é igual a {dados["Média"]} ')
#print(f'Situação é igual a {dados["Situação"]} ')
for c,v in dados.items():
    print(f'{c} é igual a {v}.')

