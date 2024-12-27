import re

def verify_password(password):
    ex = r'^(?=.*[A-Z]{3,})(?=.*[a-z])(?=.*[a-z]).{12}$'
    if re.match(ex, password):
        print("Password is strong")
    else:
        print("Password is not strong")

password = input('enter the password')
verify_password(password)



