class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("Hi, I'm " + self.name)
    def move(self):
        print("I'm walking")

class Cyclist(Person):
    # def __init__(self,name):
    #     super().__init__(name)
    def move(self):
        print("I'm cycling")

person = Person("John")
person.talk()
person.move()

cyclist = Cyclist("Jane")
cyclist.talk()
cyclist.move()