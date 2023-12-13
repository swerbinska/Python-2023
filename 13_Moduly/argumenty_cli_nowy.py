import sys
from nowy import slownie

if __name__ == '__main__':
    n = int(sys.argv[1])
    print(slownie(n))

# syst.argv to jest lista argumentow i wskazujemy jaka wartosc ma byc wyswietlona w slownie; dlatego jest int bo ma wyciagac liczbe