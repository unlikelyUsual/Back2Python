from typing import Self
# Creating a class

class Car :
    def __init__(self, color : str, house_power : int) -> None:
        self.color = color
        self.house_power = house_power
    
    def drive(self) -> None:
        print(f'It is running ..')

    def get_info(self) -> None:
        print(f"{self.color} {self.house_power}")

    def __str__(self) -> str:
        return f'{self.color} {self.house_power}'
    
    def __add__(self, other : Self) -> str :
        return f'{self.color} & {other.color}'


volvo : Car = Car('red', 200)
print(volvo)