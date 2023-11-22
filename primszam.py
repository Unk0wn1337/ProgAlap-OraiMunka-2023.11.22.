#Prímszámok kiszámolása
def primEgy(x:int):
    if x <= 1:
        print("Nem prímszám")
    elif x == 2:
        print("A 2 prímszám")
    else:
        osztoDb = 0
        for i in range(2, x-1 ,1):
            if x % i == 0:
                osztoDb += 1
        if osztoDb == 0:
            print(f"{x} prim")
        else:
            print(f"{x} nem prim")

def primKetto(x:int):
    # Optimalizálás a lépésszámra
    if x <= 1:
        print("Nem prímszám")
    elif x == 2:
        print("A 2 prímszám")
    else:
        osztoDb = 0
        index = 2
        while index < x - 1 and (x % index!=0):
            osztoDb += 1
            index += 1
        if index == x-1:
                print(f"{x} prim")
        else:
            print(f"{x} nem prim")
