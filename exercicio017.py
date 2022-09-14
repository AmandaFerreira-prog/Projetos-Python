'''seno=float(input('Comprimento do cateto oposto: '))
cos=float(input('Comprimento do cateto adjacente: '))
hip=((seno**2)+(cos**2))**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(hip))'''

import math
seno=float(input('Comprimento do cateto oposto: '))
cos=float(input('Comprimento do cateto adjacente: '))
hip=math.hypot(seno, cos)
print('O valor da hipotenusa é {:.2f}'.format(hip))