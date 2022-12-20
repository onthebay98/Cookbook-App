class Recipe:
    def __init__(self, dish, URL):
        self.dish = dish
        self.URL = URL
        self.ingredients = None
        self.preptime = None
        self.cooktime = None
        self.totaltime = None
        self.servings = None
        self.directions = None
        self.picture = None
    
    def __str__(self):
        if self.servings is None:
            self.servings = "an unspecified number of"
        
        return f"Recipe for {self.dish}. Serves {self.servings} people. From {self.URL}"
    
class Ingredient:
    def __init__(self, unit, quantity, ingredient):
        self.unit = unit
        self.quantity = quantity
        self.ingredient = ingredient
        
    def __str__(self):
        if self.unit is None:
            self.unit = ''
        if self.quantity is None:
            self.quantity = ''
        if self.ingredient is None:
            self.ingredient = ''

        return " ".join(f"{self.unit} {self.quantity} {self.ingredient}".split())