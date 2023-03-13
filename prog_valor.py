valor = float(input ('Dgite o valor do produto: '))
quantidade = int(input('Digite a quantidade comprada: '))

resultado = valor*quantidade

if resultado >= 100:
    print('Você tem', resultado * 0.1, 'reais de desconto')
    print('Valor total da sua compra', resultado - (resultado * 0.1))
    print('Obrigada pela compra!')
else:
    print('Você nao terá desconto, sua compra ficou', resultado)
    print('Obrigada pela compra!')
    
