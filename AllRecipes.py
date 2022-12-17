def allRecipesScraper(recipe):
    '''
        input: RecipeObject without ingredient or prep-time data
        
        output: RecipeObject with ingredient or prep-time data
    '''
    
    text = [x for x in BeautifulSoup(requests.get(recipe.URL).content, "html.parser").get_text().split("\n") if (x != ' ') and (x != '')]
    
    for i in range(len(text)):
        if "Prep Time:" in text[i]:
             pass
            
    return recipe

def allRecipesInitializer(URL):
    '''
        instantiates Recipe object from All Recipes URL
        
        input: All Recipes URL
        
        output: Recipe object with all data populated
    '''
    
    dish = URL.rsplit('/', 2)[1].replace('-', ' ').title() # parses recipe name from URL
    
    return allRecipesScraper(Recipe(dish, URL)) # goes to allRecipesScraper() to collect relevant information regarding recipe