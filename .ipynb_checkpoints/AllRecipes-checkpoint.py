from objects import Recipe
from objects import Ingredient
from bs4 import BeautifulSoup
import requests

from helpers import stringToMinutes

def allRecipesInitializer(URL):
    '''
        input: URL from allrecipes.com
        
        output: Recipe object with all data populated
            - dish: str
            - URL: str
            - ingredients: list of Ingredients
            - preptime: int, minutes
            - cooktime = int, minutes
            - totaltime = int, minutes
            - servings = str
    '''
    
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    
    recipe = Recipe(soup.title.string.replace(' Recipe',''), URL) # create Recipe object initialized with dish name and URL
    
    allRecipesIngredientParser(recipe, soup) # add ingredients to Recipe
    
    allRecipesTimeAndServingsParser(recipe, soup) # add prep-time and servings to Recipe
    
    return recipe

def allRecipesIngredientParser(recipe, soup):
    '''
        adds ingredients to the recipe as a list of Ingredient objects
        
        modifies recipe object
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

def allRecipesTimeAndServingsParser(recipe, soup):
    '''
        adds prep time, cooking time, total time, and serving size to Recipe object

        modifies recipe object
    '''
    recipe_attrs = soup.find("div", {"id": "recipe-details_1-0"}).find_all("div", {"class": "mntl-recipe-details__value"})
    attrs = [attribute.text.strip() for attribute in recipe_attrs] # get 5 attributes; we only need the first four
    
    recipe.preptime = stringToMinutes(attrs[0])
    recipe.cooktime = stringToMinutes(attrs[1])
    recipe.totaltime = stringToMinutes(attrs[2])
    recipe.servings = attrs[3]