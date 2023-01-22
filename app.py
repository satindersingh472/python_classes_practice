# create a class named store 
class Store:
    def __init__(self, inputName, inputProducts):
        self.name = inputName
        self.productsList = inputProducts
        def calculateInventory(self):
            for product in self.productsList:
                self.inventory = {}
                self.inventory[product] = 100
            return self.inventory

        



walmart = Store("walmart",["bread","milk","bananas","eggs"])
print(Store.calculateInventory(walmart))