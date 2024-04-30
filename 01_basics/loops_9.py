items = ["apple", "banana", "orange","apple","mango"]
unique_item=set()
for i in items:
    if i in unique_item:
        print("duplicate")
        break
    unique_item.add(i)

else:
    print("not")


        


