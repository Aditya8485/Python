"""
def translate(phrase):
    translation = ""   
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "*"
        else:
            translation = translation + letter
    return translation            

    
    
    
print(translate(input("Enter a word for checking : ")))    
"""

def lower_check(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
               translation = translation + "**"
        else:
         translation = translation + letter
    return translation


print(lower_check(input("Enter a word for checking lower case vovels : ")))



