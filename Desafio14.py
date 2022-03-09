"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca 
de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele 
desenvolveu um tabela que contém o número de itens que o cliente comprou e 
ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas 
contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi 
contratado para desenvolver o programa que monta esta tabela de preços, que 
conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
"""

# A melhor logica desse desafio seria criar um progama que faz o calculo automatico ao invés de fazer o caixa procurar o numero em uma tabela...
itens = int(input("Informe a quantidade de itens que o cliente está levando: "))

valorCompra = itens * 1.99
print(f"O valor da compra é de R${valorCompra}.")
print("1 - Dinheiro")
print("2 - Cartão")
formaPagamento = int(input("Qual será a forma de pagamento? "))

if formaPagamento == 2:
    print("Insira o seu cartão...")
    print("...")
    print("...")
    print("Transação aceita, retiro o cartão.")

else:
    troco = int(input("Informe quanto o cliente pagou para saber o troco necessario: "))

    trocoReal= troco - valorCompra
    print(f"Troco: R${trocoReal}")