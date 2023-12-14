import json

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

s = json.dumps(data) # zrzuc dane jako string - to oznacza dumpstring
print(s)
print(len(s))
print(type(s))
print()
data = json.loads(s) # ładuje string ze struktury danych
print(data)
print(len(data))
print(type(data))