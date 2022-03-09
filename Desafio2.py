"""
Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para
o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
ganhosHora = input("Quanto você ganha por hora trabalhada? ")
horasPmes = input("Quantas horas você trabalha por mês? ")
a =int(ganhosHora)
b =int(horasPmes)


salarioBruto = a*b

cortesSalariais= salarioBruto*24/100

salarioLiquido = salarioBruto - cortesSalariais

valorINSS = salarioBruto*8/100
valorSindicato = salarioBruto*5/100

print(f"Salario Bruto: R${salarioBruto}")
print(f"Salario Liquido: R${salarioLiquido}")
print(f"Valor de contribuição ao INSS: R${valorINSS}")
print(f"Valor de contribuição ao sindicato: R${valorSindicato}")
