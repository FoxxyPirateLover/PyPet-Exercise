print('Welcome to PyPet!')

name = "Fishy"
age = 5
weight = 9.5
hungry = True
photo = "<*)))><"

fish = {
    'name': 'Fishy',
    'age': 5,
    'weight': 9.5,
    'hungry': True,
    'photo': '<*(((><'
}

mouse = {
    'name': 'Mouse',
    'age': 6,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3 )~~~~',
}

pets = [fish, mouse]

print('Hello, ' + fish['name'])
print(fish['photo'])
print('Hello, ' + mouse['name'])
print(mouse['photo'])


def feed(pet):
    if pet['hungry'] == True:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else:
        print('The PyPet is not hungry!')
