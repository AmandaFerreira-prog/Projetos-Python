from time import sleep


def maior(*num):
    cont=mai=0
    print('-=-'*15)
    print('Analisando os valores passados...')
    for n in num:
        print(n,end=' ')
        sleep(0.2)
        if cont==0:
            mai=n
        else:
            if n>=mai:
                mai=n
        cont+=1
    print(f'Foram informados {len(num)} números ao todo.')
    print(f'O maior número analisado foi {mai}.')


maior(2,5,6,8,0,1,10)
maior(1,2)
maior(6,5,4)
maior(0)
