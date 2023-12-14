import requests #mogę już zaimportować bo dodalismy pakiet
from pprint import pprint #taka biblioteka jest wiec importowac mozemy
#standardowo zaczynamy pisac od importu

url = "https://api.chucknorris.io/jokes/random"
response = requests.request(method="GET", url=url) #tu podajemy jaką metodą zwracamy sie do url i skad bierzemy dane

pprint(response.json()) #tu mi sie zmieni na strukturę danych jak wywolamy response, pprint zwroci - jako slownik {}

print()
print(25*"*") #to zeby wyswietlily sie gwiazdki jako dekoracja, oddzielenie
print()
print(response.json()['value']) #wyciągnieta ze struktury danych po kluczu wartosc