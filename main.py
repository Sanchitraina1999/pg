import string
import random

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
    s = string.ascii_lowercase
    s += string.ascii_uppercase
    s += string.digits
    s += string.punctuation
    print(s)    
    length = int(input("Enter required length of password: "))
    
    