# Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
# - np. dla `73` wypisać `siedemdziesiąt trzy`

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

# _________________________________________________
# alternatywnerozwiązanie
nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_nast = {10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście",
                  19: "dziewiętnaście"}
nazwy_dziesiatek = {2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści", 5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt", 8: "osiemdziesiąt", 9: "dziewięćdziesiąt"}

nazwy_setek = {1: "sto", 2: "dwieście", 3: "trzysta", 4: "czterysta" , 5: "pięćset", 6: "sześćset", 7: "siedemset", 8: "osiemset", 9: "dziewięćset"}

liczba = int(input("Wpisz cyfre"))

g = int(liczba) // 100
d = (liczba % 100 ) // 10
j = liczba % 10
lista_2 = []
if g != 0:
    lista_2.append(nazwy_setek[g])
if d == 1:
    lista_2.append(nazwy_nast[liczba % 100])
else:
    lista_2.append(nazwy_dziesiatek[d])
    lista_2.append(nazwy_jednosci[j])
print (" ".join(lista_2) )


#nowy przykład
nastka = 15
if nastka in range(11,20):
    print("nastka")

if 11 < nastka  < 20
    print("nastka")
