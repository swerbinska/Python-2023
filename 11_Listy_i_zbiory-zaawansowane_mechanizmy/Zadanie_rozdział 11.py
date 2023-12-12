#Stworzyć * list comprehension * na podstawie jednej listy z liczbami całkowitymi, ale z elementami o 6 większymi
#Stworzyć *list comprehension* tupli składających się z w/w liczb całkowitych i ich reprezentacji jako napis
# np. `[(1, "1"), (2, "2")]`

[(x,str(x)) for x in range(10)]

#lub
t = []
for i in range(10):
    t.append([i,str(i)])
    print(t)


# biorąc słownik `{"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}` stworzyć list comprehension nazw pojazdów cięższych niż 5000
#stworzyć list comprehension nazw pojazdów cięższych niż 5000
# Nazwy podać dużymi literami (*uppercase*)


slownik_sam =  {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

[x for x in slownik_sam.keys() if slownik_sam[x] >5000]