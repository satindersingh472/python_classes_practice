class Items:
    def __init__(self, inputName, inputInventory):
        self.name = inputName
        self.inventory = inputInventory

    def __repr__(self):
        return "we have {inventory} units of {name}".format(inventory = self.inventory, name = self.name)