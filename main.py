import string
import random

def randomString(letters,stringLength=8):
    stringLength = int(stringLength)
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
    s = string.ascii_lowercase
    s += string.ascii_uppercase
    s += string.digits
    s += string.punctuation  
    length = input("Enter required length of password: ")
    print("Password: ", randomString(s,length))