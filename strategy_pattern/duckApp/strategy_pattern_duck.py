''' NOTE:
__inti__ is a method similar to constructors in C++ and Java.
Constructors contains statements or instructions that are executed at the time of object creation.'''

from fly_behaviour import *
from quack_behaviour import *

class Duck:
    # The init method or constructor
    def __init__(self, quackBehaviour, flyBehaviour):
        # Instance Variables
        self.quackBehaviour = quackBehaviour
        self.flyBehaviour = flyBehaviour

    def display(self):
        pass

    def performQuack(self):
        self.quackBehaviour.quack()

    def performFly(self):
        self.flyBehaviour.fly()

    def setQuackBehaviour(self, newquackBehaviour):
        self.quackBehaviour = newquackBehaviour

    def setFlyBehaviour(self, newflyBehaviour):
        self.flyBehaviour = newflyBehaviour


# MallardDuck inherits class Duck
# A MallardDuck by default performs SimpleQuack and FlywithWings, hence it has been hardcoded.
# We can remove this hardcoded behaviour by removing __init__ from MallardDuck class
# and passing the SimpleQuack and FlywithWings objects at the new object creation of MallardDuck
# For example, my_mallard_duck = MallardDuck(SimpleQuack(), FlywithWings())

class MallardDuck(Duck):
    # constructor for MallardDuck is assigning values to the Instance Variables defined in the SuperClass
    def __init__(self):
        self.quackBehaviour = SimpleQuack()
        self.flyBehaviour = FlywithWings()
        
    # implementing it's own display mehtod by overriding
    def display(self):
        print("I am a real Mallard Duck!!")

# RubberDuck inherits class Duck
class RubberDuck(Duck):
    def __init__(self):
        self.quackBehaviour = MuteQuack()
        self.flyBehaviour = FlyNoWay()

    def display(self):
        print("I am a yellow rubber duck!!")


# RedHeadDuck inherits class Duck
class RedHeadDuck(Duck):
    # avoiding code repeatition
    def __init__(self):
        self.quackBehaviour = SimpleQuack()
        self.flyBehaviour = FlywithWings()

    def display(self):
        print("I am a duck with a Red Head!!")
