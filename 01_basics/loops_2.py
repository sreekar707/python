number=int(input("enter your num"))
sum_of_numbers=0
for num in range(0,number):
    if(num%2==0):
        sum_of_numbers+=num
print("sum of numbers is ",sum_of_numbers)