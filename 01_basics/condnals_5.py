distance=int(input("enter distance"))
if(distance<=3):
    print("walk")
elif(distance>3 and distance<15):
    print("bike")
else:
    print("car")