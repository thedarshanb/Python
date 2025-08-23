"""Operators - Assignment, Comparision, Logical, Bitwise"""

#Operators
#Assignment Operators
a=10
a+=90
print(a) 


#Comparision Operators
a=10
b=20
print(a == b)
print(a != b)


#Logical Operators
print(True and False)
print(True or  False)
print(not(True))


#Membership Operatos
s="Darshan"
print("s" in s)
print("x" not in s)

s1="Darshan"
s2="Gowda" 
        #True     and     False      False
print(("D" in s1) and ("t" in s2))
        #True      or    False       True
print(("D" in s1) or ("t" in s2))
        #True  - False
        #False - True. in NOT operator
print(not("t" in s))


#Bitwise Operator
a = 5
b = 10
print(a & b) #And O/P = 0
print(a | b) #OR  O/P = 15
print(~a)    #NOT O/P = -6


