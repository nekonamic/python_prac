class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.li = [name, typing, reflection, year]

    def is_dynamic(self):
        if self.typing == "dynamic":
            is_dynamic = True
        else:
            is_dynamic = False
        return is_dynamic

    def __str__(self):
        if self.typing == "dynamic":
            is_dynamic = True
        else:
            is_dynamic = False
        return f"{self.name}, {self.typing} Typing, Reflection={is_dynamic}, First appeared in {self.year}"
