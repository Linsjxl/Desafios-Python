"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso
de peixes maior que o estabelecido pelo regulamento de pesca do estado de
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de 
peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos 
além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""

kg = int(input ("Quantos kgs e peixe foram trazidos para a vena hoje? "))

kgSobrando= 0

if kg <= 50:
    print("Não haverá nenhuma taxa extra.")
if kg >50:
    kgSobrando = kg-50

taxa = kgSobrando*4

if taxa > 1:
    print(f"Você trouxe {kgSobrando} kgs a mais e terá que pagar uma taxa de R${taxa} ")
