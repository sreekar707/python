string=input("enter your string")
for char in string:
    if string.count(char)==1:
        print("char is:", char)
        break

