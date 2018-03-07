a=[0,1,2,3]
b=[0,1,2,3]
dot = 0
for i in range(len(a)):
    product = a[i] * b[i]
    dot = dot + product
print(dot)
#[a*b for a,b in zip(lista,listb)] using zip