"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne por
cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.
"""

print("    CARNES:            ATÉ 5 Kg              ACIMA de 5 Kg")
print("1 - File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg")
print("2 - Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg")
print("3 - Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg")
print("A PROMOÇÃO LIMITA O CLIENTE A APENAS UM TIPO DE CARNE!!")
carne = int(input("Qual tipo de carne você irá levar? "))
quantidade = int(input("Quanto quilos dessa carne irá levar? "))
cartãoLoja = input("O cartão irá pagar com o cartão da loja? [sim,nao] ")

desconto = 0


if carne == 1:
    tipo = "File Duplo"
    if quantidade <= 5:
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.80

if carne == 2:
    tipo = "Alcatra"
    if quantidade <= 5:
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80

if carne == 3:
    tipo = "Picanha"
    if quantidade <= 5:
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if cartãoLoja == "sim":
    desconto = (preco*5)/100
    preco = preco - desconto
    pagamento = "Cartão"
else:
    pagamento = "Dinheiro"

print("NOTA FISCAL----------------------------------------------")
print("Tipo Carne   Quantidade   Preço   Pagamento   Desconto")
print(f" {tipo}        {quantidade}Kg      R${preco}   {pagamento}       R${desconto}")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
