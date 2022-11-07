val = float(input('Qual o preço do produto: R$'))
novo = val - (val * 5 / 100)
print(f'O produto que custava {val}, na promoção com desconto de 5% vai custar R$ {novo:.2f}')

