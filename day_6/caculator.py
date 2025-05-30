def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


print('***** This will print when we import this fil and also when we run directly **** ')

if __name__ == '__main__':
    print('If you run this directly it will run this print message')