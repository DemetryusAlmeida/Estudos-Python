from random import choice
nom1 = input('Nome do primeiro aluno: ')
nom2 = input('Nome do segundo aluno: ')
nom3 = input('Nome do terceiro aluno: ')
nom4 = input('Nome do quarto aluno: ')
escolhido = choice([nom1, nom2, nom3, nom4])
print('O escolhido para apagar o quadro é', escolhido)