peso=float(input('Qual o seu peso? (Kg) '))
altura=float(input('qual sua altura? (m) '))
IMC=peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}.'.format(IMC))
if IMC <18.5:
    print('Voce esta ABAIXO do peso')
elif 18.5<=IMC<25:
    print('PARABENS!, voce esta no Peso ideal!.')
elif 25<=IMC<30:
    print('Voce esta com SOBREPESO.')
elif 30<=IMC<40:
    print('Voce esta com OBESIDADE')
elif IMC>40:
    print('Voce esta com OBESIDADE MORBIDA')
