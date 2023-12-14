class Employee:
    pass


john = Employee()

john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

john.salary #tu mozemy podejrzec wynagrodzenia


class Employee:
    def __init__(self, name, dept, salary):
        self.__name = name
        self.__dept = dept
        self.__salary = salary #tu juz nie pozwoli na podejrzenie salary bo ma dwa podrkeslenia __ - to oznacza ze nie ma dostepu - linijka 25 sie nie odpali

    def get_salary(self,'Michal'):
        if user.can_access_salary(): #tu ograniczamy dostęp do wynagrodzeń np poprzez identyfikator potwierdzający uprawnienia
            return self.__salary
        else:
            return -1

    def get_salary(self):
            return self.__salary


john = Employee('John Doe', 'computer lab', 1000)
john.__salary  # error

john.get_salary()

john._Employee__salary # nazwa zmieniona do pola i wtedy za zgoda jest dostep; to nie jest intuicyjne - powinnismy korzystac z linijek 26-27



#******************************8

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    @property #oznacza ze bedzie sie zachowywac jak pola - daje pole wirtualne - nie mozna nic do niego przypisac - czyli dlatego linijka 57 jest błedna; to funkcja udajaca pole
    def r(self):
        return math.sqrt(self.x * self.x + self.y * self.y)



p = Point(3.0, 4.0)
p
print(p.r)
# p.r = 7  # error
# p.r() #przestaje byc interpretowane jako funkcja - wiec tak nie mozemy zapisac
# Anatomia obiektu

print(p.__dict__) #specjalne pole obiektu - pokazuje jak jest w srodku zbudowany obiekt - czyli ze jest slownikiem - to dziala jak __main__
print(Point.__dict__) #jaka jest klasa obiektu
