def multiply(a, b):
    # Broken version (returns addition instead of multiplication)
    return a + b 

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
