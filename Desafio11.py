"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma 
mensagem caso o valor seja inválido e continue pedindo até que o usuário 
informe um valor válido.
"""

from asyncio.windows_events import NULL

quantidade = 0

for numeros in range(0,7):
   notas = int(input("coloque uma nota: "))

maiorNumero= 0
menornumero= 0
quantidade += 1

if quantidade == 1:
    maiorNumero = menornumero = notas
else:
    if notas < menornumero:
        menornumero = notas
    
    if notas > maiorNumero:
        maiorNumero = notas
    

print(maiorNumero)
print(menornumero)