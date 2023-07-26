import math
num1 = float(input('Digite o cateto oposto: '))
num2 = float(input('Digite o cateto adjacente: '))
#hipo = math.sqrt(num1**2 + num2**2)
hipo = math.hypot(num1, num2)
print('{:.2f}'.format(hipo))