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
    