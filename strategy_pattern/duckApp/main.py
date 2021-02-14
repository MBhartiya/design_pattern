from fly_behaviour import *
from quack_behaviour import *
from strategy_pattern_duck import *

my_rubber_duck = RubberDuck()
my_rubber_duck.display()
my_rubber_duck.performQuack()
my_rubber_duck.performFly()

my_mallard_duck = MallardDuck()
my_mallard_duck.display()
my_mallard_duck.performQuack()
my_mallard_duck.performFly()
# updating the behaviour dynamically
my_mallard_duck.setFlyBehaviour(FlyNoWay())
my_mallard_duck.setQuackBehaviour(MuteQuack())
# check the updated behaviours
my_mallard_duck.performQuack()
my_mallard_duck.performFly()

my_red_duck = RedHeadDuck()
my_red_duck.display()
my_red_duck.performQuack()
my_red_duck.performFly()
