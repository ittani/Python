# Python
selft education on python
"""
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.
"""
import random
if 5 > 4:
    print("five is greater than four")
if 4 > 8:
    print("Mathematics ain't right")
    print ("Four is less than 8")
    print ("The night is still young")
#assigning operators
x=9
y="Ittani is a cool guy"
z=9.8 #double variable assigned
#printing out the values
print("her age is",x)
print(y)
"""
Type Casting 
"""
p=int(5) #Type casting
l=str("Ittani") #Type casting
print(p) 
print(l)

"""Case sensetive thing e.i"""
a=6
A="Hildah Baloyi"
#print(a)
print(A)
#Variables names
_v=8
_v1="Mufeba"
print(_v)
print(_v1)
x1,y1,p1="mike", "ado", "Bafo"
print(x1)
print(y1)
print(p1)
#Assignment

sports=["soccer","Rugby","Cricket","Formula1"]
x2,y2,z2,f2=sports
print("sports Types:",x2,y2,z2,f2)
#global variable
r="Ittani"
def Ittani():
    global r
    r="Maemo"
    print(r)
    Ittani()
print("My name is " + r)

#data types
f1=complex(4j)
print("The complex number is ",f1)
F1=complex(8j)
print("The sum of complex number is ",f1 + F1)
f2= True
if (4 < 7):
    print(f2)
F2= 8+6j
f3= -6+2j
print("The sum is ", F2 + f3) # the magic of complex numbers
print(random.randrange(1,20)) #printing a random number between 1 and 20

#length of string
a3="stellenbosch university"
print(len(a3))

#checking string
text="Ittani is doing engineering"
print("doing" in text)
#modifying strings
lop= "love is blind"
opl="HATE IS A STRONG WORD"
print(lop.upper())
print(opl.lower())

#removing white space from strings
pol="  hellow michael  "
print(pol)
print(pol.strip())

#concating strings
a5="Ittani"
b5="letitia"
c5=a5+" "+b5
print(c5)

#String format
age=25
jel="I'm ittani, and i'm {} years old"
print(jel.format(age))
year=2022
gal="The year is {}, and i'm {} years old"
print(gal.format(year,age))
"""string methods"""
t="good morning"
print(t.capitalize())

#Boolean 
print(9<0)
print (2>8)
print(4>1)
#if else statement
a=80
b=200
if a > b :
    print("a is greater than b")
else :
    print ("a is less than b")
#Boolean function e.g

def my_fun():
    return False #if a function returns true, then 
if my_fun():  
    print("Yes!") #it will print Yes!
else:
    print("NO!")
"""Python operational methods"""
#floor division'
t2=7
T2=2
print(t2 // T2) #rounds the number to the nearest whole number

#expotation
t3=2
T3=5
print(t3 ** T3) # same as 2*2*2*2*2

if t3 >= T3:
    print("2 is greater than 5")
else:
    print("2 is less than 5")
    
"""python list"""
thisls=["gippe", "G man","Thomas"]
print(thisls)
print(thisls[0])
print(thisls[2])
#list constructor
thislist= list(("lion", "seal","Elephant")) #list() is a constructor
print(thislist)
print(thislist[-1]) # -1 print the last item in the list
print(thislist[-2]) #-2 refers to the second last item
if "lion" in thislist:
    print("yes, lion is in the list")
else:
    print("No, lion is not in the list")
    
""" changing  items in the list """
thislist[1]="nooit"
print(thislist)
thislist[1:2]=["Ivan","Bafana"]
print(thislist)
#use append() to add items to the list
Thislist= ["hate","love"]
Thislist.append("wisdom")
print (Thislist)
#use insert() to instert an item at a specified index
Thislist.insert(0,"cherry")
print(Thislist)
"""Remove List Items """
school=["UP","stellies","wits","UJ"]
print(school)
school.remove("UJ")
print(school)
school.pop() #removes the last item from the list
print(school)
del school[0] # delete item from specified list
print(school)
del school #delete the entire list
school1=["ape","chip","lion"]
print(school1)
school1.clear()
print(school1)

"""Loop Lists """
school2=["ape","chip","lion"]
for x in school2:
    print(x)
print("\n Using a while loop")
i=0
while i < len(school2): #while loop
    print(school2[i])
    i=i+1

"""Sorting a list""" 
print("\n Sorted list")
school3=["Cane","Love","Aid","health","Insurance"]
school3.sort()
print(school3)
school4=[90,49,-80,6,55,35,-95]
school4.sort()
print(school4)
school4.sort( reverse= True) #sorting in descending order
print(school4)
#Python tuple
tup=("Banana","cook","orange","chicken","Air")
print(tup)
print(tup[:2])
#updating a tuple
y=list(tup)  #changing tuple value"""
y[1]="Ittani"
tup= tuple(y)
print(tup)
#adding an item to tuple
v= list(tup)
v.append("rock")
tup=tuple(v)
print(tup)
#removing items from a tuple
c= list(tup)
c.remove("Banana")
tup=tuple(c)
print(tup)
#deleting a tuple
del tup
#print(tup) #get an error message because the tuple is removed
#unpacking a tuple
print("\n unpacking a tuple")
tup1=("Banana","cook","orange","dog","snoop","orima")
(red,brown,green,*moddah)=tup1
print(red)
print(brown)
print(green)
print(moddah)
#looping through tuple
for x in tup1:
    print(x)
#looping using while loop
i=0
while i < len(tup1):
    print(tup1[i])
    i=i+1
#joining tuples together
tup2=("a","c","v")
tup3=("a1","a2","c2")
tup4=tup2+tup3
print(tup4)

# Python program to take integer, str and float inputs
#example 1
a=int(input("enter the value of a \n"))
b=int(input("enter the value of b \n"))
c=int(input("enter the value of c \n"))

if a > b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a is equal to b")

if a>c:
    print("a is greater than C")
else:
    print("a is less than C")
#example 2
name=str(input("Enter your name \n"))
surname=str(input("Enter your last name \n"))
age=int(input("Enter your age \n"))
print("name: "+name)
print("surname:"+ surname)
print("age",age)
