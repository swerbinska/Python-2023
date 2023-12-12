# Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
  - np. dla `73` wypisać `siedemdziesiąt trzy`

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_dziesiatki = {0: "", 10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "pięćdziesiat", 60: "sześćdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewięćdziesiat"}
nazwy_setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta", 400: "czterysta", 500: "pięćset", 600: "sześćset", 700: "siedemset", 800: "osiemset", 900: "dziewięćset"}
nazwy_11_19 = {0: "", 11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "piętnascie", 16: "szesnascie", 17: "siedemnascie",   18: "osiemnascie", 19: "dziewiętnascie"}

slownik = {}
n = int(input("wpisz liczbe"))
napis = nazwy_setki[n-n%100]+" "
n = n%100
if n in range(11,20):
    napis += nazwy_11_19[n]
else:
    napis += nazwy_dziesiatki[n-n%10]+ " " + nazwy_jednosci[n%10]

print(napis)