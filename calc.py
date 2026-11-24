
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"


def main():
    print("===== Python Calculator =====")

    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        result = calculate(a, b, operator)
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers")


if __name__ == "__main__":
    main()