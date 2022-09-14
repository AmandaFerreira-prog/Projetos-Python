s=n=0
for c in range(1,501,2):
    if c%3==0:
        s+=c
        n+=1
print('A soma dos {} multiplos de 3 é igual a {}.'.format(n,s))
