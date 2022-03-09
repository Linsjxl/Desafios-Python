"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o
número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
litros = int(input("Informe a quantidade de litros que você deseja colocar: "))
tipo = input(" Qual irá colocar? G- gasolina ou A- álcool? ")
tipo = tipo.upper()

gasolinaPromo = 0 
alcoolePromo= 0
gasolina = 0
alcool = 0


if tipo == "G":
    gasolina = litros*2.50
if tipo == "A":
    alcool = litros*1.90



if litros <= 20:
    gasolinaPromo = round(gasolina - (gasolina*4/100), 2) 
else:
    gasolinaPromo = round(gasolina - (gasolina*6/100), 2)

if litros <= 20:
    alcoolePromo = round(alcool - (alcool*3/100), 2)
else:
    alcoolePromo = round(alcool - (alcool*5/100), 2)



        
if tipo == "G":
    print (f"Valor final R${gasolinaPromo}.")
else:
    print (f"Valor final R${alcoolePromo}.")