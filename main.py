class Recipe:
    def __init__(self, dish, URL):
        self.dish = dish
        self.URL = URL
        self.ingredients = list()
        self.preptime = None
    
    def __str__(self):
        return f"This is a recipe for {self.dish} from {self.URL}"