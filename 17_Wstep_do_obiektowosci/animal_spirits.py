###################
# Monkey patching #
###################


class A():
    def f(self): #klasa A która ma funkcję f
        return 1


a = A()
a.f()


def f(x):
    return -1


A.f = f #podmiana w klasie i wtedy wszystkie obiekty zostaną podmienione w klasie nie tylko jeden obiekt

a.f()


###################################################

###############
# Duck Typing # funkcja wywoluje wszystko co ma takie same funkcje w ponizszym przykladzie funkcja play oznacza ze python wywoluje wszystko co ma play
###############
# w tej funkcji nie korzystamy z polimorfizmu opartego o dziedziczenie tylko z polimorfizmu obiektów ktore maja ta sama funkcję

class Drums:
    def play(self):
        return "Booom Booooom"


class Guitar:
    def play(self):
        return "Dling Dling"

class Kaczka:
    def play(self):
        return "kwa, kwa"

orchestra = [Guitar(), Guitar(), Drums(), Kaczka()]
for instrument in orchestra:
    print(instrument.play())


###################################################

################################
# We don't need no stinkin' IF # aby unikac funkcji if mozemy korzystac z polimorfizmu
################################

# Źle !
class Swallow(): #tworzymy klase jaskółka
    def __init__(self, s_type):
        self.type = s_type
        self.base_speed = 120
        self.load_factor = 15
        self.number_of_coconuts = 3

    def get_speed(self): #tu definiujemy jakie są typy jaskółki europejska, afrykańska, norweska
        if self.type == 'European':
            return self.base_speed
        elif self.type == 'African':
            return self.base_speed - self.load_factor * self.number_of_coconuts
        elif self.type == 'Norwegian':
            return self.base_speed - self.load_factor * self.number_of_coconuts * self.number_of_coconuts
        else:
            return 0


swallow = Swallow('African') #tu pytamy o prędkosc jaskółki
swallow.get_speed()

# DOBRZE !

from abc import ABC, abstractmethod


class Swallow(ABC): #stworzona abstrakcyjna jaskółka której dane beda dziedziczone
    def __init__(self, base_speed=120):
        self.base_speed = base_speed
        self.load_factor = 15
        self.number_of_coconuts = 3

    @abstractmethod #ta metoda to jest klucz bo ta funkcja definiuje sposoby liczenia predkosci dlatego dla niej jest polimorfizm
    def get_speed(self):
        pass #oznacza ze metoda jest pusta bo tu mamy abstrakcyjna metode wiec cos musimy dac, mogloby dac n = 0


class EuropeanSwallow(Swallow):
    base_speed = 120
    def get_speed(self):
        return self.base_speed


class AfricanSwallow(Swallow):
    base_speed = 200
    def get_speed(self):
        return self.base_speed - self.load_factor * self.number_of_coconuts


class NorwegianSwallow(Swallow):
    def get_speed(self):
        return self.base_speed - self.load_factor * self.number_of_coconuts * self.number_of_coconuts


swallow = AfricanSwallow()
swallow.get_speed()


# NAJGORZEJ !!!
class Swallow():
    def __init__(self):
        self.base_speed = 120
        self.load_factor = 15
        self.number_of_coconuts = 3

    def get_speed(self):
        if self.__class__.__name__ == 'EuropeanSwallow':
            return self.base_speed
        elif self.__class__.__name__ == 'AfricanSwallow':
            return self.base_speed - self.load_factor * self.number_of_coconuts;
        elif self.__class__.__name__ == 'NorwegianSwallow':
            return self.base_speed - self.load_factor * self.number_of_coconuts * self.number_of_coconuts;
        else:
            return 0


class EuropeanSwallow(Swallow):
    pass


class AfricanSwallow(Swallow):
    pass


class NorwegianSwallow(Swallow):
    pass


swallow = AfricanSwallow()
swallow.get_speed()
