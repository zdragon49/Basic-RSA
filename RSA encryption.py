from sympy import randprime
import math

plainText = input("Hello, input your text to encrypt: \n")

def stringToInt(plainText): # convert string to ascii, decdied to use ascii because it holds capital and lower case values
    integerList = []
    for i in plainText:
        integerInput = ord(i)
        integerList.append(integerInput)
    return integerList

def intToString(ascii): # convert integer to ascii
    decryptedText = ''
    for i in ascii:
        decryptedText += chr(i)  
    return decryptedText 

def pq(): # finds n
    lowerp = 2 ** (1024 - 1)  # Set the lower limit for p
    upperp = 2 ** 1024 - 1    # Set the upper limit for p

    lowerq = 2 ** (1024 - 1)  # Set the lower limit for q
    upperq = 2 ** 1024 - 1    # Set the upper limit for q 

    p = randprime(lowerp, upperp)
    q = randprime(lowerq, upperq)
    n = p * q
    n2 = (p - 1) * (q - 1)  
    return p, q, n, n2

def find_e(n2): #finds e
    # I had an issue with overflows because I was using pow and that would cause an overflow, I did some research and found that 65537 is commonly used,
    # I decided to use 65537 to circumnavigate the issue of overflows from using pow, I did include another option if 65537 was not relatively prime
    e = 65537
    if math.gcd(e, n2) == 1:
        return e
    else:
        # Fall back to a different method if 65537 is not coprime
        for i in range(3, n2, 2):
            if math.gcd(i, n2) == 1:
                return i

def find_d(e, n2): #finds d
    d = pow(e, -1, n2)  # Calculate the modular inverse
    return d

def singleASCIIEncryption(integerList, e, n): #we envrypt every letter
    encryptionList = []
    for i in integerList:
        x = pow(i, e, n)  # Use modular exponentiation 
        encryptionList.append(x)
    return encryptionList
        
def encryption(plainText): #this is the full envryption that runs everything
    p, q, n, n2 = pq()  # Generate p, q, n, n2
    e = find_e(n2)  # Find suitable e
    d = find_d(e, n2)  # Find modular inverse d
    publickey = [e, n]
    privatekey = [d, n]
    integerList = stringToInt(plainText)  # To ascii
    cipherText = singleASCIIEncryption(integerList, e, n)  # Encrypt
    print("This is encrypted:", cipherText)  # Print encrypted values
    return privatekey, publickey, cipherText

def decryption(cipherText, d, n): #we decrypt it and append it to a string
    plainTextDecrypted = []  
    for i in cipherText:
        C = pow(i, d, n)  
        plainTextDecrypted.append(C) 
    decrypted = intToString(plainTextDecrypted)  # Convert back to string
    print("This is decrypted:", decrypted)  # Print text

# Main execution
privatekey, publickey, cipherText = encryption(plainText)  # Encrypt the text
decryption(cipherText, privatekey[0], privatekey[1])  
