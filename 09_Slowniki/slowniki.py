s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'}
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a')
s.get('c', 0)
s['c'] = 3
s
del s['b']
s

s = {"a": 1, 'b': 2, 'c': 3}

for k in s.keys():
    print(k)

for k in s.values():
    print(k)

for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

s2 = {'d': 4}
s|s2

s|={'e':5}
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]}
s[2]



s={}
while True:
    wpis = input("Wpisz coś albo enter")
    if wpis == "":
        break
    print(s)
    n = s.get (wpis,0)
    n += 1
    s[wpis] = n
print (s)


Counter({'kota':2,'Ala':1,'ma':1})


lista = []
Lista.append('kota')
c = Counter(Lista)
print(c)
c = ['ala']


# Dla wczytanej liczby z wejścia z zakresu 1-999 wypisać jej postać słowną
  - np. dla `73` wypisać `siedemdziesiąt trzy`

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_dziesiatki = {10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "pięćdziesiat", 60: "sześćdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewięćdziesiat"}
# nazwy_setki = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 90: "dziewięćdziesiat"}
nazwy_11_19 = {11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "piętnascie", 16: "szesnascie", 17: "siedemnascie",   18: "osiemnascie", 19: "dziewiętnascie"}

slownik = {}
n = int(input("wpisz liczbe"))
if n in range(11,20):
    napis = nazwy_11_19[n]
else:
    napis = nazwy_dziesiatki[n-n%10]+ " " + nazwy_jednosci[n%10]

print(napis)
