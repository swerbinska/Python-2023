f = open('README.md', encoding='utf8')
#print(f) - to wyswietli tylko linijke wyzsza - dlatego musi byc potem to for line

n = 0

for line in f:
    print(f'{n:03d} {line.strip()}')
    n += 1
