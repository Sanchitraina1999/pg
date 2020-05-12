import string
import random

def randomString(letters,stringLength=8):
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
    s = string.ascii_lowercase
    s.append(string.ascii_uppercase)
    print
    s += string.digits
    s += string.punctuation  
    length = int(input("Enter required length of password: "))
    print("Password: ", randomString(s,length))