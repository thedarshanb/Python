"'While Loop, Break, Continue'"

failed=True
i=1
while failed:
     print(f"Try again{i}")
     i=i+1
 
failed =True
i=1
while True and i<=100:
     print(f"Try again!{i}")
     i=i+1


#Using Break
fail=True
i=1
while True:
     print(f"Try again{i}")
     i=i+1
     if i >100:
          break
print("I give Up")


#For print Odd number
i=1 
while i <=10:
     print(i)
     i=i+2    

#For print Even number
i=2
while i<=10:
     print(i)
     i+=2


#nested while, iteration
i=0
while i<=10:
     x=0
     while x<i:
          print("Darshan", end="+")
          x+=1
     print("")
     i+=1


#Using continue
i=0
while i<9:
    i +=1
    if i==3:
        continue
    print(i)


#Example 
pin="123"
while True:
     i=input("Enter Pin: ")
     if pin == i:
          print("Correct")
          break
     else:
          print("Incorrect")


# EX2:
pin="2025"
Trail=1
while Trail<=5:
     i=input(f"Trail-{Trail} |>>pin: ")
     Trail +=1
     if i==pin:
          print("Pin Correct")
          break
     else:
          print("Incorrect Pin")




