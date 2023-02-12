def terreno(larg, compr):
    area = larg * compr
    print(f'A area do terreno {larg}x{compr} é de {area}')


#Programa principal
l = int(input('Largura (m): '))
c = int(input('Comprimento (m): '))
terreno(l, c)