#python calculator
operator=input("enter an operator(+ _ * /):")
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

if operator == "+":
    result = num1 + num2
    print ( result )
elif operator == "_":
    result = num1 - num2
    print ( result )
elif operator == "*":
    result = num1 * num2
    print ( result )
elif operator == "/":
    result = num1 / num2
    print(result)

# python weight converter=
weight=float(input("enter your weight:"))
unit=input("kilogram or pounds? (k or l):")

if unit =="k":
    weight=weight*2.205
    unit="lbs."
elif unit =="l":
    weight=weight/2.205
    unit="kgs."
else:
    print(f"{unit}is not valid")

print(f"your weight is {weight}{unit}")

#temperature converter

temperature=float(input("enter your temperature:"))
unit=input("the unit is celcius or kelvin? (c or k):")

if unit=="c":
    temperature= temperature+273.15
    unit1="k"
elif unit=="k":
    temperature=temperature-273.15
    unit1="c"
else:
    print(f"the {unit} is not correct")

print(f"the temperature is{temperature}{unit1}")