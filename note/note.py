# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

"""
Functions

def my_function()
    #Do this
    #Then do this 
    #Finally do this

my_function()
-------------------------------
something = 123

def my_function(something)
    #Do this
    #Then do this 
    #Finally do this

my_function(123)


"""
def greet():
  print("Hello " * 3)
greet()


def greet2(n, str):
  print(str)
  if (n > 3):
    greet2(n-1, str)
greet2(5 , "Hello")

def greet3():
  print("Hello")
  print("How do you do")
  print("Isn't the weather nice today")
greet3()

"""
#Function that allows for input
name = input("Hi! what is your name?")

#This way we can call a function for specific purpose but every time we execute it, it gets modify it a little bit
def greet_with_name(name):
  print(f"Hello {name}")
greet_with_name(name)
"""

#Functions with more than 1 input

def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"How is the weather in {location}?")
greet_with("Alvin", "Hanham")


#Positional Arguments
name = "Alvin"
location = "Hanham"

def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"How is the weather in {location}?")
greet_with(name, location)

#Keyword Arguments

def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"How is the weather in {location}?")
greet_with(location = "Singapore", name = "Alice")

#Exercise Challenge 1
"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
"""
# Write your code below this line 👇
import math 

def paint_calc(height, width, cover):
  num_of_can = (height * width)/cover
  rounded = math.ceil(num_of_can) #instead of rounded(), we use this to round off to the ceilling number/whole num
  print(f"You'll need {rounded} cans of paint.")
# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Challenge 2 - Prime number checker
"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.
"""

# Write your code below this line 👇
import math

def prime_checker(number):
  if number < 2:
    print("It's not a prime number.")
    return False
  for i in range (2, math.ceil(math.sqrt(number))+1):
    if number % i == 0:
      print("It's not a prime number.")
      return False
  print("It's a prime number.")
  return True
# Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

# Method 2

# Write your code below this line 
def prime_checker(number):
  is_prime = True
  for i in range (2, number):
    if number % i == 0:
      is_prime = False #"divided evenly" in the context of prime numbers, we mean that the division result is a whole number
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number")

#Do NOT change any of the code below
n = int(input()) # Check this number
prime_checker(number=n)