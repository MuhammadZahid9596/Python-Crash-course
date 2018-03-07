fav_place={
    'zahid':['muree','lahore','kashmir'],
    'muqeet':['singapore','dubai','srilanka'],
    'ammad':['lahore','canada','karachi']
}
for name, places in fav_place.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())