km = float(input('Quantos km esse carro rodou?: '))
dia = int(input('Quantos dias ele foi alugado?: '))
p1 = dia * 60
p2 = km * 0.15
print('A pessoa terá que pagar R${:.2f}'.format(p1 + p2))