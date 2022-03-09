"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

print("Informe as suas 3 notas parciais.")
nota1= int(input("Informe a sua primeira nota: "))
nota2= int(input("Informe a sua segunda nota: "))
nota3= int(input("Informe a sua terceira nota: "))

media = (nota1 + nota2 + nota3)/3


if media < 7:
    print("Aluno reprovado.")
if media >= 7 and media != 10 :
    print("Aluno aprovado.")
if media == 10:
    print("Aluno com distinção.")
