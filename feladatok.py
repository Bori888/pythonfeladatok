def feladat_1():
    print("Írjuk ki 0-tól 150-ig a páros számokat!")
    szam = 0
    while szam <= 150:
        if szam % 2 == 0:
            print(szam , end=" ;")
            szam += 1
        else:
            szam += 1
        szam += 1

def feladat_2():
    print("Számold meg 10 bekért szám esetében a 3-mal osztható számokat!")
    szamlalo = 0
    h_oszthato = 0

    while not(szamlalo == 10):
        szamlalo += 1
        bekert = int (input('Szam:'))
        if bekert % 3 ==0:
            h_oszthato += 1
    print(h_oszthato ,"szam oszthato 3-mal")

def feladat_3():
    print("Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*")
    szam = int(input('Szam:'))
    while not ( szam % 10 == 0):
        szam =int (input('Szam:'))

def feladat_4():
    print("Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*")
    szam = int(input('Szam: '))
    while not (szam >= 10  and szam < 100 and szam % 2 == 0):
        szam = int(input('Szam: '))

def feladat_5():
    print("Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*")
    szam = int(input('Szam: '))
    while not (szam > 0 and szam % 2 == 1):
        szam = int(input('Szam: '))

def feladat_6():
    print("Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz. (és legyen pozitiv)*")
    szam = int(input('Szam: '))
    while not (szam > 0 and int(szam ** 0.5 )** 2 == szam  or szam % 3 == 0):
        szam = int(input('Szam: '))

def feladat_7():
    print("Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk! ")
    szam1 = float(input('Szam: '))
    szam2 = float(input('Szam: '))
    szam3 = float(input('Szam: '))

    while not(((szam1 + szam2) > szam3) and ((szam1 + szam3)) > szam2 and ((szam3 + szam2) > szam1) and (szam1 > 0 and szam2 > 0 and szam3 > 0)):
            szam1 = float(input('Szam: '))
            szam2 = float(input('Szam: '))
            szam3 = float(input('Szam: '))
    print("Sikeres összehoztál egy 3szöget")

def feladat_8():
    print("Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*")
    szoveg = input("3 karakteres szöveg: ")
    while not( szoveg.isalpha() and len(szoveg) == 3):
        szoveg = input("3 karakteres szöveg: ")
    print(szoveg.upper())

def feladat_9():
    print("Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*")
    szoveg = input("4 karakteres, kis betüs szöveg: ")
    while not( szoveg.isalpha() and len(szoveg) == 4 and szoveg.islower()):
        szoveg = input("3 karakteres szöveg: ")

def feladat_10():
    print("Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!")
    szam = int(input('Szam: '))
    osszeg = 0
    szamlalo = 0
    while not (szam == 0):
        szamlalo += 1
        osszeg = osszeg + szam
        szam= int(input('Szam: '))

    atlag = osszeg / szamlalo
    print(f"Az eddig meg adott szám/szamok átlaga {atlag:.2f}")

