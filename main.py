import random
#1 feladat
def beker():

    szam1 = input(print("Kérek egy páros számot! "))
    if(szam1 // 2 == 0):
        print(szam1)
    else:
        input(print("Ez nem páros! Páros számot kérek! "))

#2 feladat

def beker2(szam):
    szam1 = input(print("Kérem az első páros számot! "))
    szam2 = input(print("Kérem a második páros számot! "))
    szam3 = input(print("Kérem a harmadik páros számot! "))

    if(szam // 2 == 0):
        print(szam)
    else:
        input(print("Ez nem páros! Kérek egy páros számot"))

    szamok = list[szam1, szam2, szam3]

    i = 0
    min = 0
    while(i<len(szamok)):
        if szamok[i] < min:
            min = szamok[i]
        i+=1

    print(f"A legkisebb páros szám értéke: {min}")

def veletlenszamlista():

    veletlenlista = []
    for i in range(0,13):
        n = random.randint(-40,150)
        veletlenlista.append(n)
    print("A lista: " + veletlenlista)

    i = 0
    db = 0
    while i < len(veletlenlista):
        if(i >= 10):
            db+=1

    print(f"A kétjegyű számok száma: {db}")

    paros_osszege = []
    paratlan_osszege = []
    i = 0
    while i < len(veletlenlista):
        if(i // 2 == 0):
            paros_osszege += 1
        else:
            paratlan_osszege += 1

    print(f"A párosok összege: {paros_osszege}" f"a páratlanok összege: {paratlan_osszege}")

