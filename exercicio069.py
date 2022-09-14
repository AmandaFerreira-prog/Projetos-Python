h=t18=m20=0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade=int(input('Idade: '))
    sexo=input('Sexo [F/M]: ').upper()
    print('-' * 20)
    c=input('Quer continuar? [S/N]  ').upper()
    if sexo=='M':
        h+=1
    if idade>=18:
        t18+=1
    if sexo=='F' and idade<20:
        m20+=1
    if c=='N':
        break
print(f'Total de pessoas com mais de 18 anos: {t18}')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'E temos {m20} mulheres com menos de 20 anos.')


