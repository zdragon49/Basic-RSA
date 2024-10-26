
from sympy import randprime
import math



def stringToInt(plainText):
    integerList = []
    for i in plainText:
        integerInput = ord(i)
        integerList.append(integerInput)
    return integerList

def pq():
    lowerp = 2 ** (1024 - 1) #give the basic 1024 length
    upperp = 2 ** 1024 - 1

    lowerq = 2 **(1024-1)
    upperq = 2 ** 1024 -1 

    p = randprime(lowerp, upperp)
    q = randprime(lowerq, upperq)
    n = p*q
    n2 = (p-1)*(q-1)
    return p,q,n,n2

def finde(n2):
    for i in range(2, n2):
        if(math.gcd(i,n2) == 1):
            return i

def findd(e,n2):
    d = pow(e, -1, n2)
    return d

def encryption():
    plainText = input("Hello, input your text to encrypt")
    p,q,n,n2 = pq()
    e = finde(n2)
    d = findd(e,n2)
    publickey = [e,n]
    privatekey = [d,n]
    integerList = stringToInt(plainText) # Decided that I would use ASCII versus using integer
    
print(e)
print(n)

