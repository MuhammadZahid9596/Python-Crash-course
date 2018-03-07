topping=[]
a=input("hello start your order")
while a!='quit':
    a=input('write your order')
    if a!='quit':
        topping.append(a)
        print("you have added" + str(topping) + "to your list")
print(topping)




