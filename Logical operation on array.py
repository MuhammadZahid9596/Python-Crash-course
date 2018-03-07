#check kr rhy hain k array me elements ki jo values hain wo condition ko satisfy kr rhy hn k nhi
#25-feb-2018
import numpy as np
a = np.arange(5)
b= np.sum(a<2)
print(a)
print(a<3)
print(b)
#np. vectorize applies the to all times in an array
#np.vectorize(exp)(a)
arr = np.arange(9,0,-1)
print(arr)