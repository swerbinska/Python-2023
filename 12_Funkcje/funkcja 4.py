def _slownie999(n, jednostki=['metr', 'metry', 'metrow']):
    nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",
                      8: "osiem", 9: "dziewięć"}
    nazwy_dziesiatki = {0: "", 10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci",
                    50: "pięćdziesiat", 60: "sześćdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat",
                    90: "dziewięćdziesiat"}
    nazwy_setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta", 400: "czterysta", 500: "pięćset",
               600: "sześćset", 700: "siedemset", 800: "osiemset", 900: "dziewięćset"}
    nazwy_nastki = {0: "", 11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "piętnascie",
                16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie", 19: "dziewiętnascie"}

    ret = []

    jednosci = n % 10
    dziesiatki = n % 100 - jednosci
    setki = n - dziesiatki - jednosci

    if setki:
        ret.append((setki, nazwy_setki[setki]))

    if dziesiatki == 10 and jednosci > 0:
        nastki = 10 + jednosci
        ret.append((nastki, nazwy_nastki[nastki]))
    else:
        if dziesiatki:
            ret.append((dziesiatki, nazwy_dziesiatki[dziesiatki]))
        if jednosci:
            ret.append((jednosci, nazwy_jednosci[jednosci]))

    if ret[-1][0] in [2, 3, 4]:
        ret.append((ret[-1][0], jednostki[1]))
    elif len(ret) == 1 and ret[-1][0] == 1:
        ret = [(ret[-1][0], jednostki[0])]
    else:
        ret.append((ret[-1][0], jednostki[2]))
    return ret


def _sklej(lista):
    return [t[1] for t in lista]


print(_slownie999(3))
print(_slownie999(13))
print(_slownie999(33))
print(_slownie999(133))
print(_slownie999(333))
print(_slownie999(313))
assert _slownie999(313) == [(300, 'trzysta'), (13, 'trzynascie'), (13, 'metrow')]

print(_sklej(_slownie999(333)))
print(_sklej(_slownie999(450)))