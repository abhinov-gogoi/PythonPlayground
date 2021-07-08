class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am  {self.name}")


some_person = Person("Abhinov")
some_person.x = 3
print(some_person.x)
some_person.talk()

bob = Person("Bob Smith")
bob.talk()
