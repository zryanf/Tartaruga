from turtle import *

with open("tartaruga.txt","r") as arquivo: #lê o arquivo com as condernadas
    tartaruga = arquivo.readlines() #lê linha por linha do arq.txt
    for linha in tartaruga:
        linha = linha.split() #transforma em lista separando as palavras
        if "CIMA" in linha:
            penup()
            continue
        elif "BAIXO" in linha:
            pendown()
            continue
        setpos(int(linha[0]),int(linha[1])) #pega as coordenadas da lista
