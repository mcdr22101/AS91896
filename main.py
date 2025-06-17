"""
setting up variables and randomising next day
"""
import random
nextday=random.randint(1,7)
planeseats={"flight 1":10, "flight 2":5,"flight 3":0}
planeprice={"flight 1":100,"flight 2":150,"flight 3":200}
if nextday==7:
    planeprice={"flight 1":100*0.8,"flight 2":150,"flight 3":200}
print(nextday)
LIST_VALIDFLIGHTS = ["flight 1", "flight 2", "flight 3"]
name=("qqqqqqqqqqqqqqqqqqqqq")
"""asking the user for their name and making sure the name is not too long"""
while len(name) > 20:
 name=input("What is your name? Please enter a name shorter than 21 characters.")
print("Hello",(name)+". Please select a flight.")
x=0
"""asking user which flight they will take"""
while x==0:
    desiredflight=(input("Which flight would you like to take? " 
    "(type flight 1, flight 2, or flight 3) "))
    if desiredflight in LIST_VALIDFLIGHTS:
        x=1
desiredflightprice=(planeprice[(desiredflight)])
"""function for generating discount"""
def func_discount():
    discounteddesiredflightprice=(planeprice[(desiredflight)])*0.9
    return(discounteddesiredflightprice)
print(planeseats[(desiredflight)])
if (planeseats[(desiredflight)])>9:
    func_discount()
    """telling user whether there is a discount available or not"""
    print("There is a discount available if you fly with us tomorrow."
    "The flight will cost",(func_discount()),"NZD instead of",(desiredflightprice),"NZD.")
    if nextday==7:
        print("There is also an additional next day discount available because the next day is sunday.")
else:
    desiredflightprice=(planeprice[(desiredflight)])*1
    print("There is no discount available. Your flight will cost",(planeprice[(desiredflight)]),"NZD.")
