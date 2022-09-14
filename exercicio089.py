'''aluno=[]
boletim=[]
cont=0
while True:
    aluno.append(cont)
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[2]+aluno[3])/2)
    boletim.append(aluno[:])
    op=input('Quer continuar? [S/N] ').upper()
    if op=='N':
        break
    aluno.clear()
    cont+=1
print('-=-'*20)
print('No   Nome        Média')
print('-'*25)
p=0
total=len(boletim)
while True:
    print(f'{boletim[p][0]}   {boletim[p][1]}        {boletim[p][4]}  ')
    p+=1
    if p==total:
        break
print('-=-'*20)
while True:
    notas= int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if notas == 999:
        print('Finalizando...')
        break
    print(f'Notas de {boletim[notas][1]} são {boletim[notas][2]} e  {boletim[notas][3]}')
print('-=-'*20)
print('<<< VOLTE SEMPRE >>>')'''

boletim=[]
while True:
    nome=input('Nome: ')
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=((nota1+nota2)/2)
    boletim.append([nome,[nota1,nota2],media])
    op=input('Quer continuar? [S/N] ').upper()
    if op=='N':
        break
print('-=-'*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=-'*20)
for i,a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    op=int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if op==999:
        print('Finalizando...')
        break
    if op<=len(boletim)-1:
        print(f'Notas de {boletim[op][0]} são {boletim[op][1]}')
print('<<< VOLTE SEMPRE >>>')
