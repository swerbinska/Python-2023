lista = ['Ala', 'ma', 'kota', 'kota']

from collections import Counter
Counter(lista)
Counter({'kota': 2,'Ala': 1, 'ma': 1})


lista =[]
lista.append("ala2")
c = Counter(lista)
print(c)

c["ala2"]