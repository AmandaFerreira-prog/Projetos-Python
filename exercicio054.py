from datetime import date
atual=date.today().year
maior=menor=0
for n in range(1,8):
    ano=int(input('Em que ano a {}° pessoa nasceu? '.format(n)))
    idade=atual-ano
    if idade>=21:
        maior+=1
    else:
        menor+=1
    n+=1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E tambem {} pessoas menores de idades.'.format(menor))
