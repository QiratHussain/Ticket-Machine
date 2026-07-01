print("Welcome to the ticket machine!")
bill=0
hieght= float(input("what is your hieght?  cm"))
age=int(input("What is your age?"))
if hieght<= 120:
    print("sorry,you have to grow taller to ride.")
elif age <=4 or age> 70:
    print("Sorry,your age is not suitable for the ride.")
else: 
    print("you can take the ride.")
    if age > 18 or age<55:
        bill= 10
    else:
        bill=7
    photo= int(input('''
    Do you want photography?
    0. no
    1. yes
    '''))
    if photo==1:
        bill +=3
        print(f"You need to pay ${bill}")
    elif photo==0:
        print(f"You need to pay ${bill}")
    else: 
        print("invalid input")