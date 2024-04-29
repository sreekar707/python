string=input("enter your string ")
for char in string:
    print(char)
    if string.count(char)==1:
        print("char is ", char)
        break

