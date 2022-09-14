n=int(input('Digite um número: '))
d=0
for c in range(1,n+1):
    if n%c==0:
        print('\033[0;33m',c,end=' ')
        d+=1
    elif n%c!=0:
        print('\033[0;31m',c,end=' ')
print()
print('\033[mO número {} foi divisivel {} vezes'.format(n,d))
if d==2:
    print('E por isso ele É PRIMO!!')
else:
    print('O número {} NÃO É PRIMO!.'.format(n))