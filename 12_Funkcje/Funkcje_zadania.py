#- stworzyc słownik `{ 'first': funkcja1, 'second': funkcja2 }`, wczytać przez `input` klucz, wywołać funkcję

def Funkcja1():
    print ("funkcja1")

def Funkcja2():
    print ("funkcja2")

def funkcja_wynik():
    list_moja = {1: Funkcja1, 2: Funkcja2}
    miara = int(input("wpisz 1 lub 2"))
    return list_moja[miara]
f = funkcja_wynik()
f()
