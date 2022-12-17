class Recipe:
    def __init__(self, dish, URL):
        self.dish = dish
        self.URL = URL
        self.ingredients = None
        self.preptime = None
    
    def __str__(self):
        
        if self.preptime is None:
            self.preptime = 'unspecified'
        
        return f"This is a recipe for {self.dish} from {self.URL} with {self.preptime} prep-time"
    
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