# create a class named store 
class Store:
    def __init__(self, inputName, inputProducts):
        self.name = inputName
        self.productsList = inputProducts
    def __repr__(self):
        return "The store name is {store}".format(store =self.name)





