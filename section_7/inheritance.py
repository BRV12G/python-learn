#inheritance and polymorphism
class Animal:
    location: " australia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("speaking noww...")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")


d = Dog("Bruno")
d.speak()
