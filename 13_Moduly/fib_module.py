print("Importing " + __name__) # to bedzie wygodne gdy importujemy ten plik bo wtedy gdy odpalamy inny plik z ktorego importujemy te funkcje stad to mi sie pokarze importing i co zaimportowalam

my_variable = 7


def fib(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == '__main__': #konkstrukcja która rozpoznaje czy jest cos uruchamiane czy importowane  - taki test dla sprawdzenia czy dzialamy w tym pliku czy funkcje byly z pliku importowane i odpalane jest gdzie indziej
    print(f'Testowo: {fib(15)}')
