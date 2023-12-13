f = open('plik.txt', 'w') # pisze od poczatku wykasowujac wszystko co było a gdy damy a dodaje na koncu kolejne dane
f.write("Hello\n")
f.close() # po to aby zapisalo sie na dysku, cos jak save dla pliku (dodatkowo jest jeszcze funkcja flash -kazdy close robi wczesniej flash

#python konczac dzialanie robi close na plikach ale jesli zabraknie pradu to sie nie zakonczy wiec i nie zasefuje dlatego zawsze wprowadzamy operacje wejsica i wyjscia i powinny byc w bloku try i except i mamy blok finally ktory ma zrobic close
