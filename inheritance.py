class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("dog barks")
dog = Dog()
dog.bark()
dog.speak()

class DodChild(Dog):
    def eats(self):
        print("Drinking milk")
