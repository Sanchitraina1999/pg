import string
import random

if __name__ == '__main__':
    s = string.ascii_lowercase
    s += string.ascii_uppercase
    s += string.digits
    s += string.punctuation
    print(s)    
    length = int(input("Enter required length of password: "))
    
    