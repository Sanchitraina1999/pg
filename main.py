import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    s = s1 + s2 + s3 + s4

    print(s)    
    
    length = int(input("Enter re"))