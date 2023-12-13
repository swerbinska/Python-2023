

import sys #import wbudowanego pakietu sys gdzie jest sys.path w ktorym szuka python katalogów i modułów - wtedy szuka w biezacym katalogu i w projekcie
# python zawsze szuka domyslnie w sys.path
from fibonacci import fibonacci1 as f1

if __name__ == '__main__':
    print(sys.path)  # Tu szukamy modułów
    print(f1.fib(25))

