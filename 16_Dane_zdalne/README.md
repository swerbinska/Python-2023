# 16. Dane zdalne

- JSON - Javascript object notation
- Zdalne API - protokoły - XML-RPC, SOAP, REST - to mechanizmy przezucania danych miedzy komputeramim REST - najpopularniejszy 
- REST - REpresentational state transfer - ma zaletę - dostajemy jasona gdy wrzucamy adres internetowy z chuck.py
  - Przeglądarka a API - działa na bazie protokołu http lub https (url - universal ... location)
  - http methods 
    - `GET` - pobranie (zawsze idempotentne - nie zmienia stanu) - to co przegladarka wysyła czyli polecenie pobrania (sposób rozmowy z serwerem)
    - `POST` - tworzy zasób - submit 
    - `PUT` - zmienia zasób
    - `DELETE` - usuwa zasób
- Bibliotek `requests` - nie jest częścią pythona domyslnie - dodajemy ją do bibliotek pythona: 
- File/settings/Project:Python/ Python interpreter/ i tu sa biblioteki ktore juz mamy w pythonie - jak brakuje to dajemy "+" i wspisujemy requests - i instal package
- 
  - Instalacja
  - Użycie

można też tworzyć metody http (moduł 19)

---
# Zadanie

- Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true; Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)
- Stworzyć skrypt który z linii poleceń przyjmie nazwę kraju i dal niego wyświetli w/w dane

