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
        
# def isHungry(pet):
#     """ Determines if the pet is hungry and feeds accordingly """
#     hungryPets = [] # list to keep track of hungry pets
#     for p in pet:
#         if p['hungry'] == True: # If the value of hungry is true
#             hungryPets.append(p) # add that pet to the hungryPets list
#         else:
#             print(f"{p} is not hungry. Try again later) # if the pet is not hungry display fancy test
#     print("Pets have all been fed") 
#     hungryPets.clear() # clear the list
