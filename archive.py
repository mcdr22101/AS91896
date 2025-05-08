planeseats={"flight 1":10,"flight 2":20,"flight 3":20}
planeprice={"flight 1":100,"flight 2":150,"flight 3":200}
name=input("What is your name? ")
desiredflight=(input("Which flight would you like to take? (flight 1, flight 2, or flight 3) "))
print(planeseats[(desiredflight)])
if (planeseats[(desiredflight)])>9:
    desiredflightprice=(planeprice[(desiredflight)])*0.8
     print("There is a discount available if you fly with us tomorrow. The flight will cost",(desiredflightprice)
     "instead of",(planeseats[(desiredflight)]) )
else:
    desiredflightprice=(planeprice[(desiredflight)])*1
    print("There is no discount available.")
print(desiredflightprice)
