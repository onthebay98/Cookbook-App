from allrecipes import allRecipesInitializer

def __main__(URL):
    if "allrecipes" in URL:
        recipe = allRecipesInitializer(URL)
        return recipe
        # add some error catch for 404s?
    else:
        print("Sorry, we don't support recipes from this website yet.")
        
recipe = __main__(URL = "https://www.allrecipes.com/recipe/158799/stout-braised-lamb-shanks/")

print(recipe)

print()
print('Ingredients:')
for ingredient in recipe.ingredients:
    print(ingredient)