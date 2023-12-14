# Stworzyć skrypt który z linii poleceń przyjmie nazwę kraju i dal niego wyświetli w/w dane

import requests
from pprint import pprint
import sys

inp = sys.argv[1] #w ten sposób wywołujemy w adresie url konkretne kraje ale trzeba wlasnie
url = f"https://restcountries.com/v3.1/name/{inp}?fullText=true"
response = requests.request(method="GET", url=url)

data = response.json()[0]
pprint(data.keys())

print(f'Ludnosc:\t\t{data["population"]}')
print(f'Powierzchnia:\t\t{data["area"]}')
print(f'Waluta:\t\t\t{list(data["currencies"].keys())[0]}')
print(f'Stolica:\t\t{data["capital"][0]}')