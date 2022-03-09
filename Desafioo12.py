"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades
desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e
o total geral do pedido. Considere que o cliente deve informar quando o pedido deve 
ser encerrado.
"""

resposta = "sim"
quant = 0
quant1 = 0
quant2 = 0
quant3 = 0
quant4 = 0
quant5 = 0
preço = 0
preço1 = 0
preço2 = 0
preço3 = 0
preço4 = 0
preço5 = 0

print("Cardapio: ")
print("Especificação   Código  Preço")
print("Cachorro Quente 100     R$ 1,20")
print("Bauru Simples   101     R$ 1,30")
print("Bauru com ovo   102     R$ 1,50")
print("Hambúrguer      103     R$ 1,20")
print("Cheeseburguer   104     R$ 1,30")
print("Refrigerante    105     R$ 1,00")


while resposta in "sim":
    item = int(input("Escolha um dos intens do cardápio: "))
    quantidade = int(input("Quantos itens você deseja? "))
    resposta = str(input("Deseja continuar a compra? [sim/nao] ")).strip()[0]

    if item == 100 and quantidade!= 0:
        preço += quantidade*1.20
        quant = quantidade

    if item == 101 and quantidade!= 0:
        preço1 += quantidade*1.30
        quant1 = quantidade

    if item == 102 and quantidade!= 0:
        preço2 += quantidade*1.50
        quant2 = quantidade

    if item == 103 and quantidade!= 0:
        preço3 += quantidade*1.20
        quant3 = quantidade

    if item == 104 and quantidade!= 0:
        preço4 += quantidade*1.30
        quant4 = quantidade

    if item == 105 and quantidade!= 0:
        preço5 += quantidade*1.00
        quant5 = quantidade

preçofinal = preço + preço1 + preço2 +preço3 + preço4 + preço5

print( "Nota Fiscal: ")
print( "Especificação   Quantidade  Preço")
print(f"Cachorro Quente {quant}     R${preço:,.2f}")
print(f"Bauru Simples   {quant1}    R${preço1:,.2f}")
print(f"Bauru com ovo   {quant2}    R${preço2:,.2f}")
print(f"Hambúrguer      {quant3}    R${preço3:,.2f}")
print(f"Cheeseburguer   {quant4}    R${preço4:,.2f}")
print(f"Refrigerante    {quant5}    R${preço5:,.2f}")
print(f"Preço final:   (R${preçofinal:,.2f})")

print("Volte sempre :)")
