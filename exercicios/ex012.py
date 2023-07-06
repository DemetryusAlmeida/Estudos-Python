preco = float(input('Preço do produto: R$'))
desconto = preco / 100 * 5
print('Com 5% de desconto, o produto custará R${:.2f}'.format(preco - desconto))