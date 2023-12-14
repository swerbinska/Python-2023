#Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true; Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)
# Stworzyć skrypt który z linii poleceń przyjmie nazwę kraju i dal niego wyświetli w/w dane


import requests
from pprint import pprint

url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)
data = response.json()[0] #zamienia na słownik - wyciaga pierwszy element z listy
pprint(data.keys()) #wyswietla jakie mamy nazwy danych

print(f'Ludnosc:\t\t{data["population"]}') #wyciagamy konkretne informacje
print(f'Powierzchnia:\t\t{data["area"]}')
print(f'Waluta:\t\t\t{list(data["currencies"].keys())[0]}') #wygenerowalismy liste kluczy i wtedy pierwszy element tej listy jest brany
print(f'Stolica:\t\t{data["capital"][0]}')