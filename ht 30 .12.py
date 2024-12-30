#2
class Validate:
    def __init__(self, in_str):
        self.in_str = in_str

    def validate_string(self):
        if not (any(i.isalpha() for i in self.in_str) and any(i in "!@#$%^&*()_+-=." for i in self.in_str)):
            return "String must contain at least one alphabet and one special character"
        return "The string contains both alphabets and special characters."

user = input("Enter a string: ")
val = Validate(user)
print(val.validate_string())
print("_"*60)

#1
class Count:
    def __init__(self, in_str):
        self.in_str = in_str

    def count_characters(self):
        a_count = sum(i.isalpha() for i in self.in_str)
        n_count = sum(i.isnumeric() for i in self.in_str)
        s_count = sum(i in "!@#$%^&*()_+-?/. " for i in self.in_str)

        print(f"Alphabetic Characters: {a_count}")
        print(f"Numeric Characters: {n_count}")
        print(f"Special Characters: {s_count}")

user = input("Enter a string: ")
c = Count(user)
c.count_characters()

