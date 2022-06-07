
import requests

def recipe_search(ingredient):

    app_id = '9a400477'
    app_key = 'd12b4542139ea4eeb78f19d59269eeb6'
    result= requests.get( 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient,app_id,app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
    print(recipe['label'])
    print(recipe['uri'])


run()
