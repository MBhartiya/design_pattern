# Interface flyBehaviour
class FlyBehaviour:
    def fly(self):
        pass

# Class implementing interface FlyBehaviour
class FlywithWings(FlyBehaviour):
    def fly(self):
        print("I fly with wings")

# Class implementing interface FlyBehaviour
class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I don't fly")
