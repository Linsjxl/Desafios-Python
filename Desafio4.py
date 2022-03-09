"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota1= int(input("Insira a sua nota do primeiro bimestre: "))
nota2= int(input("Insira a sua nota do segundo bimestre: "))
nota3= int(input("Insira a sua nota do terceiro bimestre: "))
nota4= int(input("Insira a sua nota do quarto bimestre: "))

notaGeral = nota1 + nota2 + nota3 + nota4 
media= notaGeral/4

print(f"A sua media geral do ano foi {media}")
