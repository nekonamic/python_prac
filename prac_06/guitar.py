class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        if self.is_vintage():
            return f"{self.name} ({self.year}), worth $ {self.cost} (vintage)"
        else:
            return f"{self.name} ({self.year}), worth $ {self.cost}"

    def get_age(self):
        return 2021 - self.year

    def is_vintage(self):
        if self.get_age() < 50:
            return False
        else:
            return True
