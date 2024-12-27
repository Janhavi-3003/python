#def pangram(string):
"""
alphabets="abcdefghijklmnopqstuvwxyz"
    
    if  string not in alphabets:
        print("sentence must contain all alphabets")
        if not string.islower():
            print("Sentence should have lower case letters only")
            if len(string)<26 or len(string)>26:
                print("Sentence should exactly contain 26 characters")
string=input()
if pangram is string:
    print("valid")
else:
    print("invalid")
    return "sentence is valid"""
#my program:

def pangram(string):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    if not set(alphabets).issubset(set(string.lower())):
        print("Sentence must contain all alphabets")
        return False
    if not alphabets.islower():
        print("Sentence should have lower case letters only")
        return False
    if len(set(string)) != 26:
        print("Sentence should exactly contain all 26 unique characters")
        return False
    return True

string = input()
if pangram(string):
    print("Sentence is valid")


