import string 
import random

def generate_password(length, numbers=True, sp_char=True):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    characters = s1
    if numbers:
        characters += s2
    if sp_char:
        characters += s3
 
    pwd =""
    meets_criteria = False
    has_number = False
    has_special= False

    while not  meets_criteria or len(pwd) < length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in s2:
            has_number = True
        elif new_char in s3:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if sp_char:
            meets_criteria = meets_criteria and has_special

    return pwd 

length = int(input("Enter password length: "))
has_number = input("Do you want numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(length, has_number, has_special)
print("Your password is:", pwd)