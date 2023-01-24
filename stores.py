# create a class named store 
class Store:
    def __init__(self, inputName, inputProducts):
        self.name = inputName
        self.productsList = inputProducts
        self.startInventory = []


    def __repr__(self):
        return "The store name is {store}".format(store =self.name)

       

def decreaseInventory(productList,amountDecreased,productName):
            productList[0][productName] -=  amountDecreased
            return productList[0]




