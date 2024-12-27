class Calculator:
    def calculate(self, a, b=None, c=None):
        if b is None and c is None:
            return a ** 2
        elif c is None:
            return a + b
        else:
            return a * b * c
calc = Calculator()
print(calc.calculate(2))
print(calc.calculate(5, 9))
print(calc.calculate(2, 5, 9))
