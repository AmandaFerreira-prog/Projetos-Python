cadastro=[]
pessoa={}
mulheres=[]
tot=0
while True:
    Nome=input('Nome: ')
    sexo=input('Sexo: [F/M] ').upper()
    while sexo!='M' and sexo!='F':
        print('ERRO! Por Favor, digite apenas M ou F .')
        sexo = input('Sexo: [F/M] ').upper()
    if sexo=='F':
        mulheres.append(Nome)
    idade=int(input('Idade: '))
    tot+=idade
    pessoa['Nome']=Nome
    pessoa['Sexo']=sexo
    pessoa['Idade']=idade
    cadastro.append(pessoa.copy())
    op=input('Quer continuar? [S/N] ').upper()
    while op != 'S' and op!= 'N':
        print('ERRO! Responda apenas S ou N.')
        op = input('Quer continuar? [S/N] ').upper()
    if op=='N':
        break
print('-=-'*30)
media=tot/len(cadastro)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram : {mulheres}')
print('D) Lista das pessoas que estão acima da média:')
for c in cadastro:
    if c['Idade']>media:
        for p,v in c.items():
            print(f'     {p} = {v}',end='   ')
        print()
print('<<<ENCERRADO>>>')
