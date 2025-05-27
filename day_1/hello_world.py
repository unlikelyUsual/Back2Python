#Printing
print("Hello World!")


# Taking inputs 
name = input("Enter your name : ")
print("Welcome " + name + "✌️" )


#Whenever you start a new project to keep the dependency isolate from global then run this command
# command : python3 -m venv venv
# This is will create a new folder in directory with local dependency
# Then we have to activate the environment
# command :  ./venv/bin/activate
# command : source venv/bin/activate


# To install dependency from requirement.txt file run this command
# command : pip install -r ./requirement.txt

# To put dependency to requirement.txt file when you have installed new dependency
# pip freeze > requirements.txt