age=int(input ("enter age "))
day=input("enter day ")
ticket_adult=12
ticket_child=8


if age < 14 :
    if day == "wednesday":
        ticket_child=ticket_child-2
        print(ticket_child)
    else : 
        print(ticket_child)

if age >= 14 :
    if day == "wednesday":
        ticket_adult=ticket_adult-2
        print(ticket_adult)
    else :
      print(ticket_adult)

     

