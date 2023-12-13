l = list(range(5, 10))
print(l)
try:
    i = int(input("podaj indeks "))
    print(f'Pod indeksem {i} jest element {l[i]}')  # Komentarz

    # Bardzo złozona operacja sprzatania

except IndexError as e: # e to jest ten konkretny blad i wtedy on printuje rodzaj bledu
    print(e)
except ValueError as e:
    print("In Value Error")
    print(e)
except Exception as e: #ogólny błąd kiedy inne sie nie odpalaja a cos jest nie tak to idzie ten blad. i tu kolejnosc jest wazna bo program sprawdza po kolei najpierw indeks potem value i na koncu exception
    print("In Exception")
    print(e)
else:
    print("Koniec")
finally:
    print("Finally")
