class Calculator:
    def calculate(self, num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return num1 / num2
        else:
            raise KeyError(f"Invalid operation '{operation}'.")

def main():
    calc = Calculator()
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            result = calc.calculate(num1, num2, operation)
            print(f"Result: {result}")
            break
        except ZeroDivisionError as e:
            print(f"Error: {e}. Try again.")
        except ValueError:
            print("Error: Non-numeric input. Try again.")
        except KeyError as e:
            print(f"Error: {e}. Try again.")

if __name__ == "__main__":
    main()

