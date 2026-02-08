#Printing name and age using single line.
print("Name:Amrutha\nAge:20")
# Msg using Variable.
City="Guntur"
print("I live in",City)
# printing pattern using print().
print("*")
print("**")
print("***")
#Multiplication table of a number
num=5
for i in range(1,11):
    print(num,"X",i,"=",num*i)
#Printing Formatted bill
print("Item: Pen")
print("price:20")
print("Total:20")


#Storing and printing different data types
Bike_name="Royal Enfield Classic 350"   #String
BPrice=193000                           #Int
Mileage=35.5                            #float
print("Bike Name:",Bike_name,'\n',"Bike Price:",BPrice,'\n',"Mileage:",Mileage)
#Swap of two numbers without third variable
num1=100
num2=200
num1,num2=num2,num1
print("After Swap:",num1,num2)
#Converting string to int and add of two numbers
Str1="10"
Str2="20"
Str1=int(Str1)
Str2=int(Str2)
print("After convering add of numbers:",Str1+Str2)
#Simple intrest calculation using variables
p=10000
r=5
t=2
si=(p*r*t)/100
print("Simple Intrest:",si)
#Check&print of datatype of user inputs
value=10.45
print(type(value))



#Name from user and greet them
name=input("Enter your name:")
print("Good evening",name)
#Take two numbers and sum print
num1=int(input("Enter Value of num1:"))
num2=int(input("Enter Value of num2:"))
print("Sum:",num1+num2)
#Take marks of 3 subjects and print total
sub1=int(input("Enter sub1 Marks:"))
sub2=int(input("Enter sub2 Marks:"))
sub3=int(input("Enter sub3 Marks:"))
print("Total:",sub1+sub2+sub3)
#user salary and yearly income calculation
Salary=float(input("Enter your salary:"))
Yearly_Income=Salary*12
print(Yearly_Income)
#Mini User profile using inputs
name=input("enter your name:")
Age=int(input("Enter your age:"))
Gender=input("Enter your Gender:")
Profession=input("Enter your Profession:")
print("Name:",name,'\n',"Age:",Age,'\n',"Gender:",Gender,'\n',"Profession:",Profession)


#Arithmetic operations on two numbers
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print("Add:",num1+num2,'\n',"Sub:",num1-num2,'\n',"Mul:",num1*num2,'\n',"Div:",num1/num2)
#even or odd
num=int(input("Enter Value of num:"))
if(num%2==0):
    print(num ,"is Even")
else:
    print(num,"is Odd")
#greater value print 
num1=int(input("Enter value of num1:"))
num2=int(input("Enter value of num2:"))
if(num1>num2):
    print(num1,"is grater than",num2)
else:
    print(num2,"is greater than",num1)
#number check between two values
num1=int(input("Enter value of num1:"))
num2=int(input("Enter value of num2:"))
Check_for=int(input("Enter the value for check:"))
if(Check_for>num1 and Check_for<num2):
    print(Check_for,"Is i between",num1,"and",num2)
else:
    print(Check_for,"Not in between",num1,"and",num2) 
#Simple Calculator
num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
op=input("Enter operator +,-,*,/:")
if(op=='+'):
    print(num1+num2)
elif(op=='-'):
    print(num1-num2)
elif(op=='*'):
    print(num1*num2)
elif(op=='/'):
    print(num1/num2)
else:
    print("Invalid operator")


#check the num is positive or negative
num=int(input("Enter the num:" ))
if(num>0):
    print(num,"is positive")
elif(num<0):
    print(num,"is negative")
else:
    print("zero")
#eligibility check for vote
num=int(input("Enter num:"))
if(num>=18):
    print("Eligible for vote")
else:
    print("Not Eligible for vote")
#find the largest of two
num1=int(input("Enter value of num1:"))
num2=int(input("Enter value of num2:"))
if(num1>num2):
    print(num1,"is greatest")
elif(num1<num2):
    print(num2,"is greatest")
else:
    print("both are qual")
#grade based on student marks
marks=int(input("Enter the marks:"))
if(marks>=90):
    print("Grade A")
elif(marks>=75):
    print("Grade B")
elif(marks>=50):
    print("Grade C")
else:
    print("Fail")
#Electricity bill calculation
units = int(input("Enter electricity units: "))
bill = 0
if units <= 100:
    bill = units * 1
elif units <= 200:
    bill = (100 * 1) + (units - 100) * 2
else:
    bill = (100 * 1) + (100 * 2) + (units - 200) * 3
print("Total bill =", bill)
