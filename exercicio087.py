matriz=[[],[],[]]
p=pares=terceira=maior=0
while p<3:
    for c in range(0,3):
        matriz[p].append(int(input(f'Digite um valor para [{p},{c}]: ')))
        if matriz[p][c] %2==0:
            pares+=matriz[p][c]
        if c==2:
            terceira+=matriz[p][c]
        if p==1:
            if c==0:
                maior=matriz[p][c]
            else:
                if matriz[p][c]>maior:
                    maior=matriz[p][c]
    p+=1
print('-=-'*30)
print(f'''{matriz[0]}
{matriz[1]}
{matriz[2]}''')
print('-=-'*30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}.')
