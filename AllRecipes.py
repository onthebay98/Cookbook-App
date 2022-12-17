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
    
    recipe = Recipe(soup.title.string.replace(' Recipe',''), # name of dish
                    URL)
    
    return allRecipesIngredientParser(recipe, soup)

def allRecipesIngredientParser(recipe, soup):
    '''
        adds ingredients to the recipe as a list of Ingredient objects
    '''
    ingredients = set()
    
    for ultag in soup.find_all('ul', {'class': 'mntl-structured-ingredients__list'}):
        for litag in ultag.find_all('li'):
            ing = [x.text.strip() for x in litag.find_all('span')]
            
            unit = ing[0]
            quantity = ing[1]
            ingredient = ing[2]
            
            # sets attribute to None if not found in recipe
            if unit == '':
                unit = None
            if quantity == '':
                quantity = None
            if ingredient == '':
                ingredient = None
            
            ingredients.add(Ingredient(unit, quantity, ingredient))
    
    recipe.ingredients = ingredients
    
    return recipe