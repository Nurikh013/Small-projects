print("Hello, Welcome to our coffee shop!!!!!")
name=input("What is your name? \n")

print("Hello " + name + " thank you so much for coming in today!!!!")
menu="Black coffee, Espresso, Latte, Cappucino,Frappucino "
print(name + ",what would you like from our menu today. Here is what we are serving \n" + menu)
order=input()

quantity=input("How many coffees would you like?\n")
if order=="Frappucino":
    price=8
elif order=="Black coffee":
    price=6
elif order =="Espresso":
    price=4
elif order=="Latte":
    price=7
elif order=="Cappucino":
    price=5
else:
    print("Sorry, we do not have  that here.")
total=price*int(quantity)
print("Thank you.Your total is:$" + str(total)) 
print("Sounds good " + name + ",we'll have your " + quantity + " " + order + " ready for you in a moment.")
