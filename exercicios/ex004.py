#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis.
var = input('Escreva qualquer coisa: ')
print(var, 'é', type(var))
print(var, 'Só tem espaços?', var.isspace())
print(var, 'É numérico?', var.isnumeric())
print(var, 'É alfabético?', var.isalpha())
print(var, 'É alfanumérico?', var.isalnum())
print(var, 'Está em maiúsculas?', var.isupper())
print(var, 'Está em minúsculas?', var.islower())
print(var, 'Está capitalizada?', var.istitle())