"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite mais um numero: "))

if numero1 >= numero2:
    print(f"O número maior é {numero1}. ")
    if numero1 == numero2:
        print("Os dois numeros são iguais.")
else:
    print(f"O número maior é {numero2}. ")
