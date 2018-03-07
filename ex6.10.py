fav_num={
    'zahid':[2,3,4],
    'muqeet':[4,5,6],
    'ammad':[7,8,9]
}
for name, numbers in fav_num.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("- " + str(number))