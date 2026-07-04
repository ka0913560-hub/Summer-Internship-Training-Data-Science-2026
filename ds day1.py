#to write string
#print('"My" name is Khush Arora.')

#print("\nMy name is Khush Arora."
#print('''\nMy name is Khush Arora.
#I am Btech CSE student
#I study at ADGIPS.''')
#print("""\nMy name is Khush Arora.
#I am Btech CSE student
#I study at ADGIPS.""")

#various operations
#q1)
#a=21
#b=11

#a1=a+b
#a2=a-b
#a3=a*b
#a4=a/b

#print(a1,a2,a3,a4)

'''
#q2)
name="bbd"
age=25
price=99.9

print(name,age,price)

print(type(name),type(age),type(price))
'''

'''
#q3)
a=input("Enter value")
print(type(a))
    
a=int(input("Enter value"))
print(type(a))

a=float(input("Enter value"))
print(type(a))
'''


# q4 To create a basic calculator
print("\t\t\t CALCULATOR\t\t\t")
a=float(input("Enter first number"))
b=float(input("Enter second number"))
while True:
    

    print("\nChoose operation")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Percentage")
    print("6 Power")

    ch=int(input("Enter your choice(1-6)"))
    if ch==1:
        print("Addition=",a+b)

    elif ch==2:
        print("Subtraction=",a-b)
    elif ch==3:
        print("Multiplication=",a*b)
    elif ch==4:
        print("Division=",a/b)
    elif ch==5:
        print("Percentage=",(b*100)/a)
    elif ch==6:
        print("Power=",a ** b)
    else:
        print("Invalid Choice")
    c=input("\nDo you want to continue?(Y/N)")
    if c=="N" or c=="n":
        break
    



























