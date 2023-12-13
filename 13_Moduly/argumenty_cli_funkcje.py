import sys
from slownik_zadanie import funkcja_wynik


if __name__ == '__main__':
    n = sys.argv[1] #nie ma int ponieważ zwracamy artumenty opisowe: funkcja 1 i funkcja 2
    print(funkcja_wynik(n)()) #odnosimy sie do funkcji wynikowej bo ona w pliku slownik_zadanie skleja nam opisy lista_moja
