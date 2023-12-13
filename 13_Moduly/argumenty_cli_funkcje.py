import sys
from slownik_zadanie import funkcja_wynik


if __name__ == '__main__':
    n = sys.argv[1]
    print(funkcja_wynik(n)())
