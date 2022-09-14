'''matriz=[[],[],[]]
p=0
while p<3:
    for c in range(0,3):
        matriz[p].append(int(input(f'Digite um valor para [{p},{c}]: ')))
    p+=1
print(f'{matriz[0]}
{matriz[1]}
{matriz[2]}'')
'''

matriz=[[],[],[]]
for l in range(0,3):
    for c in range (0,3):
        matriz[l][c]= int(input(f'Digite um valor para [{l},{c}]:'))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()


