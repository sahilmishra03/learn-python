distance = int(input("Enter distance in km"))

if(distance<3):
    print("Cycle")
elif(distance>3 and distance<=15):
    print("Bike")
else:
    print("Car")