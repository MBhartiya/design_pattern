'''NOTE:
A class method in python always needs a self parameter because,
When you call a method on a class (such as quack() in this case), Python automatically passes self as the first argument'''

# interface QuackBehaviour
class QuackBehaviour:
    def quack(self):
        pass

# Class implementing interface QuackBehaviour
class MuteQuack(QuackBehaviour):
    def quack(self):
        print("I am Mute")

# Class implementing interface QuackBehaviour
class SimpleQuack(QuackBehaviour):
    def quack(self):
        print("I do simple quack")

# Class implementing interface QuackBehaviour
class SqueakQuack(QuackBehaviour):
    def quack(self):
        print("I do squeak quack")
