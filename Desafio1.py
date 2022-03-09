import math


tamanho= input("Informe o valor em metros quadrados da área que você deseja pintar: ")
tamanhoInt= int(tamanho)

litros= (tamanhoInt/3)

baldes=(litros/18)

baldesSugerios = (math.ceil(baldes))

preco=(baldesSugerios*80)


print(f"Será necessario um total de {baldesSugerios} baldes e o valor final da compra será R${preco}")
 

