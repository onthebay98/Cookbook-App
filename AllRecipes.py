from objects import Recipe
from objects import Ingredient
from bs4 import BeautifulSoup
import requests

from utils import stringToMinutes

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
            - directions = list
    '''
    
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    
    recipe = Recipe(soup.title.string.replace(' Recipe',''), URL) # create Recipe object initialized with dish name and URL
    
    allRecipesIngredientParser(recipe, soup) # add ingredients to Recipe
    
    allRecipesTimeAndServingsParser(recipe, soup) # add prep-time and servings to Recipe
    
    allRecipesDirections(recipe, soup) # add directions to Recipe
    
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
    timesServings = [x.replace('\n', ' ').replace("  ", " ").strip() for x in list(soup.find("div", {"id": "recipe-details_1-0"}))[1].text.strip().split('\n\n\n')]
    timesServingsDict = dict(x.split(": ") for x in timesServings)

    if 'Prep Time' in timesServingsDict:
        recipe.preptime = stringToMinutes(timesServingsDict['Prep Time'])
        
    if 'Cook Time' in timesServingsDict:
        recipe.cooktime = stringToMinutes(timesServingsDict['Cook Time'])

    if 'Total Time' in timesServingsDict:
        recipe.totaltime = stringToMinutes(timesServingsDict['Total Time'])
        
    if 'Servings' in timesServingsDict:
        recipe.servings = stringToMinutes(timesServingsDict['Servings'])
        
def allRecipesDirections(recipe, soup):
    recipe.directions = [x.text.strip() for x in soup.find("div", {"id": "recipe__steps-content_1-0"}).find_all("p")]