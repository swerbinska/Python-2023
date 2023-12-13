import sys
def Funkcja1():
    return("funkcja1")


def Funkcja2():
    return("funkcja2")

list_moja = {'1': Funkcja1, '2': Funkcja2}

def funkcja_wynik(miara):
    return list_moja[miara]


if __name__ == '__main__':
    print(sys.argv)
    klucz = sys.argv[1]
    print(klucz)
    print(list_moja[klucz]())

