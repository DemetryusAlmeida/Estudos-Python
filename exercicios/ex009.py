n = int(input('Escreva um número: '))
print('-' * 12)
for i in range(0, 11):
    n2 = i * n
    print('{} x {:2} = {}'.format(n, i, n2))
print('-' * 12)