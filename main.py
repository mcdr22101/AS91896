"""
setting up variables
"""
LIST_VALIDFLIGHTS = ["flight 1", "flight 2", "flight 3"]

"""name asking function"""
str_name=("")
def func_nameask():
    name=input("What is your name? ")
    return(name)
func_nameask()
print("Hello",(name)+". Please select a flight.")
dict_planeseats={"flight 1":10,"flight 2":20,"flight 3":20}
dict_planeprice={"flight 1":100,"flight 2":150,"flight 3":200}
x=0
while x==0:
    desiredflight=(input("Which flight would you like to take? (type flight 1, flight 2, or flight 3) "))
    if desiredflight in LIST_VALIDFLIGHTS:
        x=1
        

print(planeseats[(desiredflight)])
if (planeseats[(desiredflight)])>9:
    desiredflightprice=(planeprice[(desiredflight)])
    discounteddesiredflightprice=(planeprice[(desiredflight)])*0.8
    print("There is a discount available if you fly with us tomorrow. The flight will cost",(discounteddesiredflightprice),"instead of",(desiredflightprice))
else:
    desiredflightprice=(planeprice[(desiredflight)])*1
    print("There is no discount available.")
print(desiredflightprice)
