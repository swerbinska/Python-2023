class MyClass:
    i = 12345 #pole klasy, rekordy

    def __init__(self, n): #metoda specjalna bo ma podkreslniki, jest to funkcja ktora jest wywolywana gdy tworzymy dany obiekt; ma dwa parametry: self - pokazuje obiekt na samego siebie, i kazda metoda ma tego selfa, oraz n - mowi co ma ustawic self na n
        self.n = n

    def f(self): #metoda - funkcja składowa klasy, mówi co mozna  ztymi rekordami zrobic
        return f'hello world {self.n}'


o1 = MyClass(1) #tworze obiekt pierwszy i przekazuje mu argument 1
o2 = MyClass(2)
o3 = MyClass("Ala")

o1

o1.i #mamy dwa obiekty o1 i o2 ktore maja wspólne i
o2.i
o1.n
o2.n
o1.f()
o2.f() #ta kropka oznacza włóż o1 do f czyli do selfa
o3.f()

class MyClass:
    i = 0

    def __init__(self, n):
        self.i += 1
        self.n = n

    def f(self):
        print(self)
        return f'hello world {self.n}'

    @classmethod
    def get_i(cls):
        print(cls)
        return cls.i


o1 = MyClass(1)
o2 = MyClass(2)

o1.i
o2.i
o1.n
o2.n
o1.f() #ta kropka oznacza włóż o1 do f czyli do selfa
o2.get_i()

MyClass.get_i()
