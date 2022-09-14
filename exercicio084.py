cadastro=[]
pessoa=[]
gorda=[]
magra=[]
n = 0
maior=menor=0
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    cadastro.append(pessoa[:])
    n+=1
    if n==1:
        maior=menor=pessoa[1]
    else:
        if pessoa[1]>maior:
            maior=pessoa[1]
        elif pessoa[1]<menor:
            menor=pessoa[1]
    op=str(input('Quer continuar? [S/N] ')).upper()
    if op=='N':
        break
    pessoa.clear()
for p in cadastro:
    if p[1]==maior:
        gorda.append(p[0])
    elif p[1]==menor:
        magra.append(p[0])
print('-='*25)
print(f'Ao todo voce cadastrou {len(cadastro)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de {gorda}')
print(f'O menor peso foi de {menor}Kg. Peso de {magra}')


