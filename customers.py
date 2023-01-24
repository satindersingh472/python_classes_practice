class Customers:
    def __init__(self,inputName,inputAge):
        self.name = inputName
        self.age = inputAge

    def __repr__(self):
        return "{name} is a {age} years of age.".format(name = self.name, age=self.age)