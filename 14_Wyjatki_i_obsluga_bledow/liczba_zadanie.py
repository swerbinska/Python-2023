# wczytaj przy użyciu `input` liczbę; wypisz sumę jej cyfr; jeśli podano błędne wejście, poproś jeszcze raz

while True:
    try:
        a = int(input('podaj liczbe dwucyfrowa'))

        if a in range(11,100):

            b = a // 10  # – daje cyfrę dziesiątą
            c = a % 10  # – daje cyfre jednosci
            i = c + b

            print(i)

        else:
            print("blad")

    except IndexError as e:
        print(e)
    except ValueError as e:
        print("In Value Error")
        print(e)
    except Exception as e:
        print("In Exception")
        print(e)
    else:
        break
    finally:
        print("Finally")
