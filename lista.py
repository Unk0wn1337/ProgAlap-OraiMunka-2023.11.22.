#Generálj 5 véletlen számot 10 és 35 között
import math
import random


def veletlen():
    lista = []
    index = 0
    while index < 5:
        szam = math.floor(random.random()*(35-10)+10)
        lista.append(szam)
        index+=1
        return  lista
    print(f"Random számok: {lista}")
listam = veletlen()


# def listaKiir(lista):
#    for i in range(0,len(lista-1)):
#        print(f"A lista {i}. eleme {lista[i]}")

def listaKiirKetto(listam):
    index = 0
    while index < len(listam):
        print(listam[index])
        index+=1

