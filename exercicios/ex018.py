from math import radians, sin, cos, tan
num = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(num))
cos = cos(radians(num))
tan = tan(radians(num))
print('O seno desse ângulo é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(seno, cos, tan))