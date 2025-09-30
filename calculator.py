def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

if __name__ == "__main__":
    print("Basic Calculator - Standard Order of Operations")
    print("Available operations: +, -, *, /")
    print("Enter your calculation as a standard math expression (e.g., 2 + 3 * 4 - 5 / 2)")

    expr = input("Enter your calculation: ")
    try:
        # Only allow safe characters
        allowed = set("0123456789+-*/. ()")
        if not set(expr).issubset(allowed):
            raise ValueError("Invalid characters in input.")
        # Replace division by zero with error message
        if "/ 0" in expr.replace(' ', ''):
            print("Error: Division by zero")
        else:
            result = eval(expr)
            print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"Error: {e}")
