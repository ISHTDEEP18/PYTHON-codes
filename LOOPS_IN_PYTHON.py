#WHILE LOOP = execute some code WHILE some condition remains true

#1=
name = input("enter your name:")

while name == "":   #WHILE THIS CONDITION IS TRUE
    print("you did not enter your name")#EXECUTE THIS CODE UNLESS
    # CONDITION BECOMES FALSE AS LOOP
    name= input("enter your name:")  #AGR YEH LINE NA LIKH KR SIRF UPR
    # KA PRINT WALA LIKHTE TO "YOU DID NOT ENTER YOUR NAME" KA INFINITE LOOP CHLEGA

print(f"Hello {name}!")

#2=
age=int(input("enter your age ="))

while age <0:
    print("age can't be negative")
    age=int(input("enter your age ="))

print(f"you are {age} years old!")

#3=
food=input("enter a food you like (q to quit):")

while not food == "q": #until this condition isn't true
    print(f"you like {food}") #loop this
    food=input("enter another food you like (q to quit):") #loop this
 #when entered q then print bye!
print("bye!")



#FOR LOOPS

for x in range(1,11):#range is an exclusive fn so 11 tk krne pr 10 tk aayega 11 excluded
    print(x)

for x in reversed(range(1,11)):#reversed gives reverse counting
    print(x)

for x in range(1,11,2):#counts odd only
    print(x)

for x in range ( 1, 21):
    if x==13:
        continue #to skip over an itteration
    else:
         print ( x )

for x in range ( 1, 21):
    if x==13:
        break #breaks the itteration at the provided point
    else:
        print ( x )


#TIME WATCH

import time
time1=int(input("enter the time in seconds: "))

for x in range(0, time1):
    print(x)
    time.sleep(1)

print("Times up!")

#DIGITAL CLOCK

import time
time1=int(input("enter the time in seconds: "))

for x in reversed(range(0, time1)):
    seconds=x % 60
    minutes=int(x/60) % 60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")  #:02 means 0 padding of 2 digit
    time.sleep(1)

print("Times up!")



#NESTED LOOP = LOOP WITHIN ANOTHER LOOP(OUTER,INNER)
#OUTER LOOP:
#     INNER LOOP:


for x in range(3):
    for y in range(1,10):
        print(y,end="")
    print()


#PROGRAM TO MAKE A SYMBOLIC RECTANGLE

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol= input("Enter a symbol to use: ")

for x in range(rows):
   for y in range(columns):
       print(symbol, end="")
   print()