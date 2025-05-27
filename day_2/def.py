from datetime import datetime

#function definition 
def show_date () -> None:
    print("Current time", datetime.now())


def show_name(name:str) -> None:
    print("hello", name)


def add(a : float, b : float) -> float: 
    return a + b


print(add(1,2))