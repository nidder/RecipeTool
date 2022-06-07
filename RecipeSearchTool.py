import requests


def recipe_search(ingredient):

    app_Id ='9a400477'
    app_Key ='d12b4542139ea4eeb78f19d59269eeb6'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_Id, app_Key)
    response = requests.get(url)
    data = response.json()
    return data ['hits']


def run():
    ingredient = input('Enter ingredient:')
    customers = float(input('How many people do you need to cook/bake for?'))
    results = recipe_search(ingredient)


    for result in results:
        recipe = result['recipe']


    if customers == recipe['yield'] or customers < recipe['yield']:
        print ('This recipe will make enough for your requirement of {} people.'.format(customers))
    else:
        print('This recipe will need to be adjusted to make enough for your requirements.')
    print('This recipe will make enough for {} people.'.format(recipe['yield']))
    print(recipe['label'])
    print(recipe['shareAs'])

run()











