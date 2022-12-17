from main import Recipe
from main import Ingredient
from bs4 import BeautifulSoup
import requests

def allRecipesInitializer(URL):
    '''
        input: URL from allrecipes.com
        
        output: Recipe object with all data populated
    '''
    
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    
    recipe = Recipe(str(soup.title)[len('<title>'):len(str(soup.title))-len(' Recipe</title>')], # name of dish
                    URL)
    
    return recipe