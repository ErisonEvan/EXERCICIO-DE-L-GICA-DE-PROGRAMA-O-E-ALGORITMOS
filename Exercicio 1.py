print('Bem-vindo a loja do Erison Evangelista de Lima')  # Mostrando na tela um mensgem de boas vindas
valor = float(input('Entre com o valor do produto: '))  # Pedindo para que o cliente digite o preço do produto
qtd = int(input('Entre com a quantidade do produto: '))  # Pedindo para que o cliente digite a quantidade do produto
if (qtd < 200):
    produto = valor * qtd  # Criando uma variavel produto
    desconto = produto * 0.0  # Criando uma variavel desconto
elif (200 <= qtd < 1000):
    produto = valor * qtd
    desconto = produto * 0.05
elif (1000 <= qtd < 2000):
    produto = valor * qtd
    desconto = produto * 0.1
else:
    (qtd >= 2000)
    produto = valor * qtd
    desconto = produto * 0.15
print('O valor SEM desconto: {}'.format(produto))  # Mostrando na tela uma mensagem com o produto SEM desconto
print('O valor COM desconto: {}'.format(produto - desconto)) # Mostrando na tela uma mensagem com o produto COM desconto
