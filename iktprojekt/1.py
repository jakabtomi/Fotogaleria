import random
import string

def veletlen_szamok():
    also_hatar = int(input("Add meg a legkisebb szamot: "))
    felso_hatar = int(input("Add meg a legnagyobb szamot: "))
    darab = int(input("Hany darab szamot szeretnel generaltatni? "))
    
    szamok = [str(random.randint(also_hatar, felso_hatar)) for _ in range(darab)]
    
    
    with open("ki.txt", "a") as f:
        f.write(";".join(szamok) + "\n")  
    
    print(f"A generált számok: {';'.join(szamok)}")

def veletlen_szovegek():
    darab = int(input("Hany darab szoveget szeretnel generaltatni? "))
    
    szovegek = []
    for _ in range(darab):
        hossz = random.randint(1, 20)
        szoveg = ''.join(random.choice(string.ascii_letters) for _ in range(hossz))
        szovegek.append(szoveg)
    
   
    with open("ki.txt", "a") as f:
        f.write(";".join(szovegek) + "\n")  
    
    print(f"A generált szövegek: {';'.join(szovegek)}")

def ellenoriz_szamokat():
    also_hatar = int(input("Add meg a legkisebb szamot: "))
    felso_hatar = int(input("Add meg a legnagyobb szamot: "))
    
    try:
        with open("ki.txt", "r") as f:
            tartalom = f.readlines()  
            for sor in tartalom:
                szamok = list(map(int, sor.strip().split(";")))  
                megfelel = all(also_hatar <= szam <= felso_hatar for szam in szamok)
                
                if megfelel:
                    print(f"A fájlban lévő számok ebben a sorban megfelelnek: {szamok}")
                else:
                    print(f"A fájlban lévő számok nem felelnek meg ebben a sorban: {szamok}")
    
    except FileNotFoundError:
        print("A ki.txt fájl nem található.")
    except ValueError:
        print("A fájl nem csak számokat tartalmaz.")

def ellenoriz_szovegeket():
    try:
        with open("ki.txt", "r") as f:
            tartalom = f.readlines()  
            for sor in tartalom:
                szovegek = sor.strip().split(";")
                megfelel = all(1 <= len(szoveg) <= 20 and szoveg.isalpha() for szoveg in szovegek)
                
                if megfelel:
                    print(f"A fájlban lévő szövegek ebben a sorban megfelelnek: {szovegek}")
                else:
                    print(f"A fájlban lévő szövegek nem felelnek meg ebben a sorban: {szovegek}")
    
    except FileNotFoundError:
        print("A ki.txt fájl nem található.")

def main():
    print("Valassz a lehetosegek kozul:")
    print("1. Veletlen szamok generalasa")
    print("2. Veletlen szovegek generalasa")
    print("3. Szamok ellenorzese fajlbol")
    print("4. Szovegek ellenorzese fajlbol")
    
    valasztas = input("Add meg a valasztott lehetoseg szamat (1-4): ")
    
    if valasztas == '1':
        veletlen_szamok()
    elif valasztas == '2':
        veletlen_szovegek()
    elif valasztas == '3':
        ellenoriz_szamokat()
    elif valasztas == '4':
        ellenoriz_szovegeket()
    else:
        print("Ervenytelen valasztas, kerlek 1 es 4 kozott adj meg egy szamot.")

if __name__ == "__main__":
    main()
