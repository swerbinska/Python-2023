z = set(range(10))
z
z = {1, 2, 3, 4, 1, 2}
z
z = {'a', 'b', 'c'}
z
'a' in z #czy a należy do zbioru?
'd' in z
'd' not in z #czy d nie nalezy do zbioru?
z2 = {'a', 'b', 'c', 'd'}
z < z2 # czy z zabiera sie w z2?
z3 = {'d', 'e'}
z | z3
z & z2
z & z3
z2 - z
z2 ^ z3

slownik = {z: 3}  # Błąd
fz = frozenset(z)
slownik = {fz: 3}
slownik
zwykly_zbior=set(fz)
zwykly_zbior