"""Tuples, Sets, Dictionaries in python"""

#Tuples
Tuple=("Apple","Banana","Orange") 
Number=(1,3,2,4,5,7)
print(Tuple)           #Output: ('Apple', 'Banana', 'Orange')
print(Number)          #Output: (1, 3, 2, 4, 5, 7)

#Accesing Tuple Elements
fruits=("Orange","Apple","Kiwi")
print(fruits[0])         #Output: Orange
print(fruits[-1])        #Output: Kiwi

#slicing Tuple
print(fruits[1:3])       #Output: ('Apple', 'Kiwi')


#Tuple Operations
Tuple1=(1,2,3)            
Tuple2=(4,5,6)
combine=Tuple1 + Tuple2
print(combine)           #Output: (1, 2, 3, 4, 5, 6)

#Tuple Repetition
Repeat=(0,0,7)*2         #Output: (0, 0, 7, 0, 0, 7)
print(Repeat)

#Tuple Methods, 
# .count()
Tuple=(1,2,3,4,1)
print(Tuple.count(1))       #Output: 2

# .index()
x=("Fish","Chicken","Goat")
print(x.index("Goat"))       #Output: 2

"'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#Sets
"'sets Operations'"

set1={1,2,3,7}
set2={4,5,6,7}
print(set1 | set2) #Union Output: {1, 2, 3, 4, 5, 6,7}

print(set1 & set2) #Intersection Output: {7}

print(set1 ^ set2) #Difference Output: {1, 2, 3, 4, 5, 6}

"'Set Methods"

vehicles={"Car","Bus","Jeep"}

vehicles.add("Bike")
print(vehicles)          #Output: {'Car', 'Bus', 'Bike', 'Jeep'} 

vehicles.remove("Bike")
print(vehicles)          #Output: {'Car', 'Bus', 'Jeep'}

vehicles.discard("Jeep")
print(vehicles)          #Output: {'Car', 'Bus'}

vehicles.pop()  #Randomly remove the elements, Output: {'Car'}
print(vehicles)

vehicles.clear()
print(vehicles)


"'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

#Dictonaries Operations
Demo={
     "Key1":"Value 1",
     "Key2":"Value 2"
}
print(Demo["Key1"])

food={"Mysore":"Mysore paka",
      "Mandya":"Ragi Muddai",
      "Manglore":"NeerDosa",
      "Bengaluru":"Pizza"}
print(food["Mysore"]) 

print(food["Mandya"])


#Accesing dictonary elements
print(food.get("Manglore"))

print(food.get("Shivmogga","NotFound"))

#Add and Update of elements

#Add
food["Bellari"]="Rotti"
print(food)

#Update
food["Mysore"]="Mailari Dosa"
print(food)

#Removing Elements
food.pop("Mysore")
print(food)

del food["Bengaluru"]
print(food)

food.clear()
print(food)


#Dictonary Methods
Dict={"Manglore":"Neer Dosa", "Mysore":"mysorepaka", "Bengaluru":"Pizza"}

print(Dict.keys())

print(Dict.values())

print(Dict.items())

new={"Hubbali":"Rotti"}
food.update(new)
print(food)

Dict["Bengaluru"]=("Burger")
print(Dict)