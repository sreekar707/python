number=int(input("enter your number"))
is_prime=True

if number>1:
    for i in range(2,number):
        if(number%i)==0:
            is_prime=False
            break


    else:
        print(is_prime)