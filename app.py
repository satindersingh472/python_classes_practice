# create a class named store 
class Store:
    def __init__(self, inputName, inputProducts):
        self.name = inputName
        self.productsList = inputProducts
        



walmart = Store("walmart",["bread","milk","bananas","eggs"])
print(walmart.name)