s1=float(input('Primeiro segmento: '))
s2=float(input('Segundo segmento: '))
s3=float(input('Terceiro segmento: '))
if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
    print('Os segmentos acima podem formar um TRIANGULO',end=' ')
    if s1!=s2!=s3!=s1:
        print('ESCALENO!')
    elif s1==s2==s3:
        print('EQUILATERO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO!')