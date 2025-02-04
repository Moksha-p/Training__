class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def __str__(self):
        return f"Bird: {self.name}, Can Fly: {self.can_fly}"

class Fish(Animal):
    def __init__(self, name, can_swim):
        super().__init__(name)
        self.can_swim = can_swim

    def __str__(self):
        return f"Fish: {self.name}, Can Swim: {self.can_swim}"

bird = Bird("Parrot", True)
fish = Fish("Goldfish", True)

print(bird)
print(fish)
