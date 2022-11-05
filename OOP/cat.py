from animal import Animal
class Cat (Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height

    def showInfo(self):
        print("I'm " + self.name)
        print(" age " + str(self.age))
        print(" height " + str(self.height))