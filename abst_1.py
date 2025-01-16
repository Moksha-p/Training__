from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def travel(self):
        pass

class Bus(Transport):
    def __init__(self, route):
        self.route = route

    def travel(self):
        return f"Bus {self.route} is traveling"

class Train(Transport):
    def __init__(self, route):
        self.route = route

    def travel(self):
        return f"Train {self.route} is traveling"

bus = Bus("10A")
train = Train("Express")
print(bus.travel())
print(train.travel())