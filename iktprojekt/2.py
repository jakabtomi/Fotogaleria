def beolvas_fajlbol(fajlnev):
    try:
        with open(fajlnev, 'r') as f:
            adatok = f.read().splitlines()  
        return adatok
    except:
        print("Hiba: A fájl nem található.")
        return None

def eldonto(adatok):
    if all(x.isdigit() for x in adatok): 
        return [int(x) for x in adatok] 
    elif all(isinstance(x, str) for x in adatok):  
        return adatok  
    else:
        print("Hiba: Vegyes típusú adatok!")
        return None

def csere_rendezes(lista, novekvo=True):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if (novekvo and lista[i] > lista[j]) or (not novekvo and lista[i] < lista[j]):
                lista[i], lista[j] = lista[j], lista[i]  
    return lista

def beszurasos_rendezes(lista, novekvo=True):
    for i in range(1, len(lista)):
        kulcs = lista[i]
        j = i - 1
        while j >= 0 and ((novekvo and lista[j] > kulcs) or (not novekvo and lista[j] < kulcs)):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = kulcs
    return lista

def beszuras(lista, uj_elem, novekvo=True):
    lista.append(uj_elem) 
    return beszurasos_rendezes(lista, novekvo)  

def main():
    fajlnev = "ki.txt"
    adatok = beolvas_fajlbol(fajlnev)  
    
    if adatok is None:
        return  

    adatok = eldonto(adatok)  

    if adatok is None:
        return  

    print("Válassz rendezési sorrendet:")
    print("1. Növekvő")
    print("2. Csökkenő")
    
    sorrend_valasztas = input("Sorrend választás (1 vagy 2): ")
    novekvo = True if sorrend_valasztas == "1" else False

    print("Válassz rendezési algoritmust:")
    print("1. Csere rendezés")
    print("2. Beszúrásos rendezés")

    algoritmus_valasztas = input("Algoritmus választás (1 vagy 2): ")

    if algoritmus_valasztas == "1":
        rendezett_adatok = csere_rendezes(adatok, novekvo)  
    else:
        rendezett_adatok = beszurasos_rendezes(adatok, novekvo)  

    print("Rendezett lista:", rendezett_adatok)

    uj_elem = input("Adj meg egy új elemet: ")
    if uj_elem.isdigit():  
        uj_elem = int(uj_elem)

    uj_lista = beszuras(rendezett_adatok, uj_elem, novekvo)
    print("Új lista:", uj_lista)

main()
