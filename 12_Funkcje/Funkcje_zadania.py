# - stworzyc słownik `{ 'first': funkcja1, 'second': funkcja2 }`, wczytać przez `input` klucz, wywołać funkcję

def Funkcja1():
    print("funkcja1")


def Funkcja2():
    print("funkcja2")


def funkcja_wynik():
    list_moja = {1: Funkcja1, 2: Funkcja2}
    miara = int(input("wpisz 1 lub 2"))
    return list_moja[miara]


f = funkcja_wynik()
f()


# _____________________________________________
# stworzyc funckcję `alphabet_range` działająca jak `range` ale dla liter (z trzema parametrami - `start`, `end`, `step`)
# przykład: `alphabet_range('E')` -> `['A', 'B', 'C', 'D']` - albo jeszcze lepiej generator
# użyć
# `ord` - podaje kod calkowity danego znaku
# `chr` - podaje znak odpowiadający danemu kodowi całkowitemu

def alphabet_range(start, end, step):
    return (chr(x) for x in range(ord(start), ord(end), step))


alphabet_range("a", "f", 1)

list(alphabet_range("a", "f", 1))


# drugie rozwiazanie:
def alphabet_range(start="A", end="z", step=1):
    return (chr(x) for x in range(ord(start), ord(end), step))


list(alphabet_range(end="M"))


# stworzyć funkcję `slownie_do999()` która zwróci słownie liczbę z zakresu 0-999
# stworzyć funkcję pomocniczą `_slownie_do999()` zwracającą listę tupli `(wartość, słownie)` dla 1 i "nastek" , 10, 100
# stworzyć funkcję pomocniczą `_sklej()` sklejającą w/w listę
# stworzyć funkcję `dodaj_jednostke` przyjmującą w/w listę i 3 formy np. `['jabłko', 'jabłka', 'jabłek']`
# zbudować funkcję `słownie` podającą słownie liczby całkowite do miliardów (do `999_999_999_999`)


nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_dziesiatki = {0: "", 10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "pięćdziesiat", 60: "sześćdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewięćdziesiat"}
nazwy_setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta", 400: "czterysta", 500: "pięćset", 600: "sześćset", 700: "siedemset", 800: "osiemset", 900: "dziewięćset"}
nazwy_11_19 = {0: "", 11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "piętnascie", 16: "szesnascie", 17: "siedemnascie",   18: "osiemnascie", 19: "dziewiętnascie"}

slownik = {}
n = int(input("wpisz liczbe"))
napis = nazwy_setki[n-n%100]+" "
n%= 100
if n in range(11,20):
    napis += nazwy_11_19[n]
else:
    napis += nazwy_dziesiatki[n-n%10]+ " " + nazwy_jednosci[n%10]

print(napis)

def slownie_do999(napis):




