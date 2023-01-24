# create a class named store 
class Store:
    def __init__(self, inputName, inputProducts):
        self.name = inputName
        self.productsList = inputProducts
        self.startInventory = []
        for product in inputProducts:
            self.startInventory.append(100)
        self.productsInventory = []
        self.productsInventory.append(dict(zip(inputProducts,self.startInventory)))

       

def decreaseInventory(productList,amountDecreased,productName):
            productList[0][productName] -=  amountDecreased
            return productList[0]
walmart = Store("walmart",["bread","milk","bananas","eggs"])
print(walmart.productsInventory)
print(decreaseInventory(walmart.productsInventory, 50, "milk"))

