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


#_____________________________________________
# stworzyc funckcję `alphabet_range` działająca jak `range` ale dla liter (z trzema parametrami - `start`, `end`, `step`)
  #przykład: `alphabet_range('E')` -> `['A', 'B', 'C', 'D']` - albo jeszcze lepiej generator
  #użyć
  #`ord` - podaje kod calkowity danego znaku
  #`chr` - podaje znak odpowiadający danemu kodowi całkowitemu

def alphabet_range(start, end, step):
    return[chr(x) for x in range(ord(start),ord(end),step)]
alphabet_range("a","f",1)

list(alphabet_range("a","f",1))