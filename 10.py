"'For loops | Range, Enumerate, Nested Loop"
    
#Syntax
#for item in sequences:

for i in range(1,10):
     print(i)


cities=["Bengaluru","Mysuru","Mandya"]
for city in cities:
     print(city)


#2. Using range() with for Loops
for i in range (1,11,2):
     print(i)

print("Break")

for j in range(2,12,2):
     print(j)


#3. Looping Over strings
name="Karnataka"
for letter in name:
     print(letter)


#4. Using enumerate
l="name"
for l in enumerate(l):
     print(l)


cities=["Mandya","Mysore"]
for index, city in enumerate(cities):
     print(f"city{index+1} : {city}")


l=[1,2,3,4,5]
for index, l in enumerate(l):
     print(f"{l} -- {index}")


#5. Using if, else condition
cities=["Mandya","Mysore","Bengaluru"]
trail=1
if trail<3:
     for city in cities:
          city=input("Enter Your city: ")
          trail+=1
          if city in cities:
               print("Found it")
          else:
               print("Not Found")


#Example 

for i in range(1,11):
    print(f"{2}x{i}={2*i}")
    
for i in range(1,11):
     for j in range(1,11):
          print(f"{i}x{j}={i*j}")
     print()



