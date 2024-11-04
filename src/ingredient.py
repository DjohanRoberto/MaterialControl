class Ingredient:
    # Arguments : 
    #   name = string
    #   unit = float
    #   price = float
    def __init__(self, name, unit, price):
        self.name = name
        self.unit = unit
        self.price = price
        self.ppu = price / unit

    def edit(self, name, unit, price):
        self.name = name
        self.unit = unit
        self.price = price
        self.ppu = price / unit