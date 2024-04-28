password=input("enter your password")


if(len(password)<6):
    print("weak")
elif(len(password)>=6 and len(password)<=10):
    print("medium")
else:
    print("strong")
    