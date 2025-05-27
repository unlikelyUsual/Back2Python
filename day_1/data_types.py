# Data types
# Basic
number : int = 10
decimal : float = 10.23
text : str = "Hello, There"
active : bool = True

# Composite
name : list = ['list item 1','list item 2', 'list item 3' ] # lists
coordinate : tuple = (1.5, 2.5) # tuples : like list but cannot modify 
unique : set = {1,4,2,9}
data : dict = {'name' : 'bob', 'age' : 20}


# Parsing 
year : float = float(input("Enter you birth year"))
age : str = 2025 - year
print("Age " + str(age))


# String methods 
course : str = "Python course"
print(course.find('y')) # return index
print(course.replace('course', 'x')) # replace course with x
print("course" in course) # true


# Arithmetic
print(10/3) # float value
print(10//3) # whole value
print(10 ** 2) # 10 ^ 2
