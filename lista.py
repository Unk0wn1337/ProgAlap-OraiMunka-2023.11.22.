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
    print(f"Random számok: {lista}")

