rivers = {
    'Nile':'Egypt',
    'Indus':'Pakistan',
    'Thames':'USA'
}
for river,country in rivers.items():
 print(river.title()+ " "+ "flows in"+ " " + country.title())
print("\nThese are the rivers in the list")
for river in rivers.keys():
    print("River" + " " +river.title() + " " +"is in the list")
print("\nThese countries ar ein list")
for country in rivers.values():
    print("The country" + " " +country.title()+ " " + "is in the list")