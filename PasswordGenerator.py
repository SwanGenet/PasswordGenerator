from random import *

def password_generator():
    size = int(input("Password Length : "))
    caps = str(input("Allow Uppercase : (y or n) "))
    symbols = str(input("Allow Symbols : (y or n) "))
    numbers = str(input("Allow Numbers : (y or n) "))
    char = 'abcdefghijklmnopqrstuvwxyz'
    
    if caps == 'y':
        char += char.upper()
    if symbols == 'y':
        char += '+!.?@#$%€'
    if symbols == 'y':
        char += '0123456789'
    
    password = ""
    i = 0
    while i < size:
        password += char[randint(0,len(char)-1)]
        i += 1
    return password

print('Password : ', password_generator())