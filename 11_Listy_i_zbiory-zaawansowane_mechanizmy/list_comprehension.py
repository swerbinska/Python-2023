range(10)

list(range(10))

(x * x for x in range(10)) # generator

[x for x in range(10)]

[x * x for x in range(10)] # lista

[x for x in range(10) if x % 2 == 0]

[x * x for x in range(10) if x % 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)]

{x for x in range(10)} #tworzenie zbioru

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0} #dictionary comprehension

kwadraty = []
for i in range(10):
    if i % 2 = 0:
        kwadraty.append(i * i)

print(kwadraty)

print([i * i for i in range(10) if i % 2 = 0])


kwadraty = []

for i in range(10):
    kwadraty.append(i*i)

print(kwadraty)


print([i*i for i in range(10)])

kwadraty = []

for i in range(10):
    if i % 2 == 0:
        kwadraty.append(i * i)

print(kwadraty)

print([i * i for i in range(10) if i % 2 == 0])
