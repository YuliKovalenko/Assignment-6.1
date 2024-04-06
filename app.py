def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    while True:
        operation = input("Enter operation (+ or -): ")
        if operation not in ("+", "-"):
            print("Invalid operation. Please enter '+' or '-'.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)

        print(f"Result: {result}")

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() not in ("y", "yes"):
            break