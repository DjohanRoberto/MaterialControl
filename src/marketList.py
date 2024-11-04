

class MarketList:
    def __init__(self):
        self.mList = {} # Market List

    # Adds a new caterogy to the list
    ######################################
    # Arguments : 
    #   categoryName = string
    # Return:
    #   1 = success
    #   0 = fail
    ######################################
    def addCategory(self, categoryName):
        #check if catergory already exists 
        if categoryName in self.mList:
            return 0
        #add the category
        self.mList[categoryName] = []
        return 1

    # Adds a new item to  category in the list
    ######################################
    # Arguments : 
    #   ingredient = Ingredient(class)
    #   category = string
    # Return:
    #   1 = success
    #   0 = fail
    ######################################
    def addItem(self, ingredient, category):
        if category not in self.mList:
            return 0
        if ingredient not in self.mList[category]:
            self.mList[category].append(ingredient)
        else:
            return 0
        return 1
    
    # change a caterogy name that exist in the list
    ######################################
    # Arguments : 
    #   old = string
    #   new = string
    # Return:
    #   1 = success
    #   0 = fail
    ######################################
    def editCategory(self, old, new):
        if old in self.mList:
            self.mList[new] = self.mList[old]
            return 1
        return 0
    
    # edit an item in the list
    ######################################
    # Arguments : 
    #   ingredient: Ingredient(class)
    #   name : string
    #   unit : float
    #   price : float
    # Return:
    #   1 = success
    #   0 = fail
    ######################################
    def editItem(self, ingredient, name, unit, price):
        ingredient.edit(name, unit, price)

