"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente
a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

print("Responda todas as perguntas com sim ou não.")
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")


pergunta1 = pergunta1.upper()
pergunta2 = pergunta2.upper()
pergunta3 = pergunta3.upper()
pergunta4 = pergunta4.upper()
pergunta5 = pergunta5.upper()

resultado1 = 0
resultado2 = 0
resultado3 = 0
resultado4 = 0
resultado5 = 0


if pergunta1 == "SIM":
    resultado1= 1
if pergunta2 == "SIM":
    resultado2= 1
if pergunta3 == "SIM":
    resultado3= 1
if pergunta4 == "SIM":
    resultado4= 1
if pergunta5 == "SIM":
    resultado5= 1

soma = resultado1 + resultado2 + resultado3 + resultado4 + resultado5

if soma <= 1:
    print("O individuo é inocente.")
if soma == 2:
    print("O individuo é um suspeito.")
if soma == 3 or soma == 4:
    print("O individuo é um cumplice.")
if soma == 5:
    print("o individuo é o assasino.")