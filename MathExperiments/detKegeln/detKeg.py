from sympy import *
import numpy as np
import scipy.stats as ss

init_printing(use_unicode=True)


def getR():
    x = np.arange(0, 10)
    xU, xL = x + 0.5, x - 0.5 
    prob = ss.norm.cdf(xU, scale = 3) - ss.norm.cdf(xL, scale = 3)
    prob = prob / prob.sum() #normalize the probabilities so their sum is 1
    num = np.random.choice(x, size = 1, p = prob)
    return num[0]

arr=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
choosen=[-1]
while -1 in arr:
    num=getR()
    print(num)
    x = int(input("Enter fieldnumber: "))
    if x in range(0,9) and x not in choosen:
        choosen.append(x)
        arr[x]=num

m=np.array(arr)
m=m.reshape((3,3))
d=np.linalg.det(m)
print(d)