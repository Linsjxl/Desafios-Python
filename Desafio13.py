"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com 
os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

divida = float(input("Insira aqui o Valor da divida: "))

juros10 = (divida*10)/100
divida10 = divida + juros10
parcela3 = divida10 / 3

juros15 = (divida*15)/100
divida15 = divida + juros15
parcela6 = divida15 / 6

juros20 = (divida*20)/100
divida20 = divida + juros20
parcela9 = divida20 / 9

juros25 = (divida*25)/100
divida25 = divida + juros25
parcela12 = divida25 / 12


print("Valor divida   Juros   Parcelas   Valor Parcela")
print(f"  R${divida}       R$0       1          R${divida}")
print(f"  R${divida10}      R${juros10}     3          R${parcela3:,.2f}")
print(f"  R${divida15}      R${juros15}     6          R${parcela6:,.2f}")
print(f"  R${divida20}      R${juros20}     9          R${parcela9:,.2f}")
print(f"  R${divida25}      R${juros25}     12         R${parcela12:,.2f}")