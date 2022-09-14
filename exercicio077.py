'''vogal=('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
vogais='A','E','I','O','U'
for p in vogal:
    print(f'\nNa palavra {p} temos',end=' ')
    for v in vogais:
        if v in p:
            print(v,end='  ')'''
vogal=('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for p in vogal:
    print(f'\nNa palavra {p} temos',end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra,end='  ')

