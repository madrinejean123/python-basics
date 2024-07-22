class Animal:
    
    def __init__(self,name) -> None:
        self.name = name
    def speak(self):
       raise NotImplementedError ("subclass must implement abstract")
class Dog(Animal):
    def speak(self):
            return f"{self.name}says woof"
class Cat(Animal):
    def speak(self):
            return f"{self.name}says mweow"
class Cow(Animal):
     def speak(self):
            return f"{self.name} says moo"
dog = Dog("jacx")
cat = Cat("jeep")
cow = Cow("chos")
        
print(dog.speak())
print(cat.speak())
print(cow.speak())