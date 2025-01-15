class Appliance:
    def turn_on(self):
        return "Appliance is turned on"

class WashingMachine(Appliance):
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        return f"Washing Machine {self.model} is turned on"

appliance = Appliance()
washing_machine = WashingMachine("LG")
print(appliance.turn_on())
print(washing_machine.turn_on())