from operator import truediv
from tkinter import YView

print("hello world")
#this is comment
print("damn")
#strings
mail = "div@1234"
print(f"your email is: {mail}")
#integers
age = 19
print(f"my age is: {age} years old")
#float(number with decimal)
price = 10.99
print(f"price of object is: ${price}")
#boolean(true/false)
student = True
print(f"Are you a student: {student}")
#boolean example {if,else}
is_student = False
if is_student:
    print(f"are you a student: {is_student}")
else:
    print ("you are not A student")

#TYPECASTING = process of converting one datatype to other
#str(),int(),float(),bool()
name="harry"
age=19
price=1.99
is_student=True
#1.float to integer
price=int(price)
print(price)
#2.integer to float
age=float(age)
print(age)
#3.integer to string
age=str(age)
print(age)
#str to boolean
name=bool(name)
print(name)
#input
name=input("what is your name?")
print(f"hello {name}!")
#ARITHMETIC OPERATORS
friends=10
#friends=friends + 1
#friends += 1 #augumented addn. operator
#friends=friends _ 2
#friends -= 2 #augumented subt. operator
#friends=friends * 3
#friends*= 3 #augumented subt. operator
#friends=friends / 2
#friends/= 2  #augumented div. operator
#friends=friends ** 2  # **= means to the power of
#friends**=2 #augumented expon. operator
#end=friends % 3 # % = modulus - means it gives remainder
#print(end)

# PYTHON BUILT IN ARITHMETIC OPERATORS
x = 3.14
y = 4
z = 5
result = round(x)
result = abs(y)
result = pow(4, 3)
result = max(x, y, z)
result = min(x, y, z)
print(result)

import math

x = 9.9
print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x)
result = math.floor(x)
print(result)



# logical operators evaluate multiple conditions (or, and, not)
#or = at least one condition must be True
#and = both conditions must be True
#not = inverts the condition (not False, not True)

#OR=
temp = 20
is_raining = True
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

#AND=
temp = 20
is_sunny: True
#if temp >= 28 and is_sunny:
    #print("It is HOT outside")
    #print("It is SUNNY")
#elif temp <= 0 and is_sunny:
   # print("It is COLD outside ")
  #  print("It is SUNNY ")
#elif 28 > temp > 0 and is_sunny:
    # print("It is WARM outside")
    # print("It is SUNNY")

#conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#Print or assign one of two values based on a condition
# x if condition else y
num = 5
a = 6
b=7
age = 13
temperature = 20
user_role= "admin"
#print("Positive" if num > e else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num = a if a >b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather "HOT" if temperature > 20 else "COLD"


#STRINGS (ABOUT)

name=input("enter your full name:")

#result=len(name)
#result=name.find("o")
#result=name.rfind("q")
#result=name.isdigit()
#result=name.isalpha()
#name=name.capitalize()
#name=name.upper()
#name=name.lower()
print(result)



#INDEXING= accessing elements of a sequence using [] (indexing operator)
           # [start : end : step]

credit_number = "1234-5678-9012-3456"
# print(credit_number[0])
#print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
#print(credit_number[-1])
#print(credit_number[::3])

credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")


#format specifiers = {value:flags} format a value based on what #
#flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

