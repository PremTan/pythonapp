import random
import datetime

# global list declaration
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
# global variable declaration

i = 0

# Home function
def Home():
    
    print("\t\tWELCOME TO HOTEL DARBAR\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Room Service (Menu Card)\n")
    print("\t\t\t 4 payment\n")
    print("\t\t\t 5 Record\n")
    print("\t\t\t 0 Exit")

    ch = int(input("-->"))

    if (ch==1):
        print(" ")
        Booking()
    
    elif(ch==2):
        print(" ")
        Rooms_info()

    elif(ch==3):
        print(" ")
        restaurant()

    elif(ch==4):
        print(" ")
        Payment()

    elif(ch==5):
        print(" ")
        Record()

    else:
        exit()

# Function used in bookings

def Booking():
    print("BOOKING ROOMS")
    print(" ")

    while True:
        n = str(input("Name : "))
        p1 = int(input("phone No. : "))
        a = str(input("Address : "))
        
        # check if any field is not empty
        if n!="" and p1!="" and a!="" :
            name.append(n)
            add.append(a)
            break
        
        else:
            print("\tName. Phone no. & Address cannot be empty..!!")
        
    cii = str(input("Check-In : "))
    checkin.append(cii)










# Function calling
Home()