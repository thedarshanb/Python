#string Manipulation

#concatenation using + operator
First="Darshan"
Last="Gowda"
Full=First + " " + Last
print(Full)


#Repetition
message= "Warning! " *10
print(message)

#String Methods
string="Darshan"
print(string.upper())
print(string.lower())
print(string.strip()*2)
print(string.replace("Darshan","Gowda"))


#for single line string 
single='Darshan said "hello"'
print(single)


#for multi line
Multi='''Darshan Said "Hi"
        I said "Hello"
        '''
print(Multi)


#for finding length of string
message="This is warning!"
print(len(message))


#string Slicing
Name="Darshan"
print(Name[0:2]) #Index Position -1
print(Name[2:4])
print(Name[4:])
print(Name[:7])

print(Name[-7:]) #-ve Indexing
print(Name[-3:])
print(Name[-5:-3])
print(Name[:-5])

print(Name[::2]) #[start:end:step]

#Escape Sequences
Intro="My Name is \n Darshan" # \n for nextline
print(Intro)

Intro="My Name is \t Darshan" # \n for tabspace
print(Intro)







