pets = []
pet = {
    'name':'puppy',
    'owner':'Philip'
}
pets.append(pet)
pet = {
    'name':'meow',
    'owner':'James'
}

pets.append(pet)
pet = {
    'name':'Bull',
    'owner':'Ramesh'
}
pets.append(pet)
for pet in pets:
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))