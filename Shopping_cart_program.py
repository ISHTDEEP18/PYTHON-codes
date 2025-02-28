
foods=[] #ek food ki list
prices=[] #ek price ki list
total=0
while True:
     food=input("enter a food you like to buy(q to quit): ")
     if food.lower() =="q":
        break #yeh to bs hai ki q se quit wrna infinite food ask krlo.
     else:
          price=float(input(f"enter the price of the {food}: $")) #price inputting
          foods.append(food) #add food
          prices.append(price) #add price

print("------YOUR CART------")

for food in foods: #range of all food taken
    print(food,end=" ") #by using end printed horizontally
    total += price
print()
print(f"your total is: ${total}")



