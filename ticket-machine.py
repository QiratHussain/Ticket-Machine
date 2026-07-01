print("Welcome to the ticket machine!")
hieght= float(input("what is your hieght?  cm"))
if hieght<= 120:
    print("sorry,you have to grow taller to ride.")
else: 
    print("you can take the ride.")
    age= int(input("What is your age?"))
    if age > 18:
        bill= 10
    else: 
        bill= 7
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