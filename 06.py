"'+++++++++++++++++++List operations & Methods++++++++++++++++++++++++++++++++'"

#Lists

items=["Egg,onion,Tea"] #By adding the elements in list
print(items)

mixing=["Apple",100,[1,2],True] #By adding types of datatypes in list                                 
print(mixing[1]) #O/P : 100


# Initial list
i = ["EGG", "Fish", "Chicken", "Mutton"]

i.pop(0)
print(i)   # Output: ['Fish', 'Chicken', 'Mutton']


i.append("Veg")
print(i)   # Output: ['Fish', 'Chicken', 'Mutton', 'Veg']

i.remove("Veg")
print(i)   # Output: ['Fish', 'Chicken', 'Mutton']

i.insert(1,"Veg")
print(i)   # output: ['Fish', 'Veg', 'Chicken', 'Mutton']

i[0] = "Fish Fry" # output: ['Fish Fry', 'Veg', 'Chicken', 'Mutton']
print(i)

i.extend(["Chicken Curry","Mutton Curry"])
print(i)

i.clear() # output: []
print(i)

#copy
a=[1,2,5,7]
b=a.copy()
print(b)   #output: [1, 2, 5, 7]


#List Slicing
i=["a","b","c","d"]
print(i[1:2])  #output: ['b']

i2=i[1:3]
print(i2)      #output: ['b', 'c']

print(i[1:3])  #output: ['b', 'c']


#Finding length in list
i=["Coffee","Milk","Sugar"]
print(len(i))                   #output:  3

#Sorting Method 
Numbers=[1,2,10,5,15,20,25,50]
print(sorted(Numbers))          #output: [1, 2, 5, 10, 15, 20, 25, 50]

#sum Method
Num=[1,2,10,17] 
print(sum(Num))                 #output: 30

mix=[2,2.5,2.5]
print(sum(mix))                 #output: 7.0

#Common Methods
fruits=["Bannana","Apple","orange"]
print(fruits.index("Apple"))     #index(element)/ output: 1

numbers=[1,4,5,10,5,5]
print(numbers.count(5))          #count(element)/  output: 3

fruits.reverse()
print(fruits)                    #reverse(element)/ output: ['orange', 'Apple', 'Bannana']




#Nested List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])     # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)
print(matrix[1][2])  # Output: 6
print(matrix[2][0])  # Output: 7
print(matrix[2][2])  # Output: 9

