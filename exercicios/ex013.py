salario = float(input('Quanto este funcionário ganha?: R$'))
aumento = salario / 100 * 15
print('Este funcionário recebia R${:.2f}, com o aumento de 15%, receberá R${:.2f}'.format(salario, salario + aumento))