mbs = int(input("Informe qual é o tamanho em Mb do arquivo que você deseja baixar: "))
mbps = int(input("Agora informe em mbps a velocidade atual aproximada da sua internet: "))

mbpsReal = mbps/8

tempo = round(mbs/mbpsReal)

print(f"O seu arquivo levará em média {tempo} segundos para ser baixado.")