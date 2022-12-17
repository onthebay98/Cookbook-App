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
    def __init__(self):
        self.unit = None
        self.quantity = None
        self.ingredient = None