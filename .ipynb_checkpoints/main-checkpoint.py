from allrecipes import allRecipesInitializer
from utils import minutesToString

def __main__(URL):
    if "allrecipes" in URL.lower():
        recipe = allRecipesInitializer(URL)
        return recipe
        # add some error catch for 404s?
    else:
        print("Sorry, we don't support recipes from this website yet.")

print('Enter the URL of your recipe:')
URL = str(input())

recipe = __main__(URL)

def printRecipe(recipe):
    print()
    print()
    print()
    print()
    print()

    print(recipe)

    print()
    print('Ingredients:')
    for ingredient in recipe.ingredients:
        print(ingredient)

    print()
    print(f'Total cook time: {minutesToString(recipe.totaltime)}')


    print()
    directions = recipe.directions

    for i in range(len(directions)):
        print(f'Step {i+1}: {directions[i]}')
        print()

    print()
    print()
    print()
    print()

printRecipe(recipe)