cities = {
    'Karachi' : {
        'country':'Pakistan',
        'population': 250000,
         'fact':'city of lights'
         },
    'Mumbai' : {
         'country':'India',
        'population': 450000,
         'fact':'Busiest indian city'
    },
    'Multan': {
         'country':'Pakistan',
        'population': 150000,
         'fact':'city of saints'
    }
}
for city,info in cities.items():
    country=info['country'].title()
    population=info['population']
    fact=info['fact'].title()
    print('\n' +city.title() + ' is in country ' + country)
    print('its population is' + str(population))
    print('and this city is' + fact)