"'Conditional Statments [if, elif, else]'"

#if condition

time=10
if time == 10:
     print("Its a dinner time")


#else condition

else:
     print("Its not a dinner time")


#elif condition

time=int(input("Enter Timmings: "))
if time == 9:
    print("Its time for Breakfast")
elif time == 1:
    print("Its time for Lunch")
elif time ==10:
    print("Its time for Dinner")
else:
    print("Its not a time for meals")


#Ex1 voting 

vote=int(input("Enter Your Age: "))
if vote >= 18:
    print("Your are eligible for voting")
else:
    print("Your not eligible for voting")



#Ex2 Using logical operator

age=int(input("Enter Your Age: "))
is_student = False
if age < 18 or is_student:
    print("Your are eligible for student discount")
else:
    print("Your not eligible for student discount")



#Ex3 Checking Bus Ticket Prices

age = int(input("Enter your age : "))
if age < 5:
    print("Ticket is free")
elif age <=12:
    print("child discount")
elif age >= 60:
    print("Your are a Senior citizen discount.")
else:
    print("you pay the full fare.")



# Nested if statements

day = input("Enter the day: ").lower()
is_raining = False
if day == "saturday" or day == "sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")






        


