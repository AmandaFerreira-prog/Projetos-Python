l=float(input('Largura da parede: '))
a=float(input('Altura da parede:'))
area=l*a
litros=area/2
print('Sua parede tem dimensão de {}X{} e sua área é de {}m2'.format(l,a,area))
print('Para pintar essa parede, voce precisara de {} de tinta'.format(litros))