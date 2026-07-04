#Data Science Day4

#Topic - OOPS
'''
#Class eg
class account:
    pass
a1=account()
a2=account()
a3=account()

print(a1)
print(a2)
print(a3)
'''

#Q1. Student Information System
#Create a Student class with attributes: Name, Roll Number, Marks (3 subjects).
#Methods: get_data(), display_data(), calculate_percentage().

'''
class student:
    def get_data(self):
        self.name=input("Enter name=")
        self.roll=int(input("Enter roll number="))
        self.m1=float(input("Enter marks of subject 1="))
        self.m2=float(input("Enter marks of subject 2="))
        self.m3=float(input("Enter marks of subject 3="))

    def calculate_percentage(self):
        self.percentage=(self.m1+self.m2+self.m3)/3
        

    def display_data(self):
        print("\n\n\t\t\t\tStudent details\n")
        print("Name=",self.name)
        print("Roll number=",self.roll)
        print("Subject 1 marks=",self.m1)
        print("Subject 2 marks=",self.m2)
        print("Subject 3 marks=",self.m3)
        print("Total Percentage=",self.percentage,"%")

s1=student()

s1.get_data()
s1.calculate_percentage()
s1.display_data()
'''

'''
#Q2. Bank Account
#Create a BankAccount class with Account Holder Name, Account Number, Balance.
#Methods: deposit(), withdraw(), display_balance().
#Conditions: Deposit must be positive and withdrawal cannot exceed balance


class BankAccount:
    name="Khush Arora"
    aa_no=121121
    password="1234"
    balance=50000
    def deposit(self):
        pwd=input("Enter Password:")
        if pwd==self.password:
            amt=float(input("Enter deposit amount"))
            if amt>0:
                self.balance=self.balance+amt
                print("Amount Deposited successfully")
            else:
                print("Deposited amount must be positive")
        else:
            print("Wrong password")

    def withdraw(self):
        pwd=input("Enter Password:")
        if pwd==self.password:
            amt=float(input("Enter withdrawl amount"))
            if amt<= self.balance:
                self.balance=self.balance-amt
                print("Withdrawl siccessful")
            else:
                print("Insufficent balance")
        else:
            print("Wrong password")

    def display_balance(self):
        pwd=input("Enter Password:")
        if pwd==self.password:
            print("\n\n\t\t\t\tACCOUNT DETAILS\n\n")
            print("Account holder name:",self.name)
            print("Account number:",self.aa_no)
            print("Total balance:",self.balance)
        else:
            print("Wrong password")

a1=BankAccount()



while True:
    print("\n\n\t\t\tBANK MANAGEMENT SYSTEM\n\n")
    print("\n1 Deposit")
    print("\n2Withdraw")
    print("\n3 Display Balance")
    print("\n4 Exit")

    ch=int(input("Enter choice"))

    if ch==1:
        a1.deposit()
    elif ch==2:
        a1.withdraw()

    elif ch==3:
        a1.display_balance()

    elif ch==4:
        print("Thank you")
        break

    else:
        print("Invalid choice")
        
'''

'''
#Q7. Shape Area Calculator
#Create Shape parent class.
#Child classes: Circle, Rectangle, Triangle.
#Each class should implement its own area() method.


class shape:
    def area(self):
        print("Area of shape")

class circle(shape):
    def area(self):
        r=float(input("Enter raidus of circle"))
        a=r*(22/7)*r
        print("Area of circle is:",a)
        

class rectangle(shape):
    def area(self):
        l=float(input("Enter length of rectangle"))
        b=float(input("Enter breadth of rectangle"))
        a=l*b
        print("Area of rectangle is:",a)
        

class triangle(shape):
    def area(self):
        h=float(input("Enter height of triangle"))
        b=float(input("Enter base of triangle"))
        a=(b*h)/2
        print("Area of rectangle is:",a)


while True:
    print("\n\n\t\t\tSHAPE AREA CALCULATOR\n\n")
    print("\n1 Circle")
    print("\n2 Rectangle")
    print("\n3 Triangle")
    print("\n4 Exit")
    ch=int(input("Enter your choice"))

    if ch==1:
        c=circle()
        c.area()
    elif ch==2:
        r=rectangle()
        r.area()
    elif ch==3:
        t=triangle()
        t.area()
    elif ch==4:
        print("Thank you")
        break
    else:
        print("Invalid choice")
    
'''


'''
#Q5. Vehicle Management System
#Create a Vehicle base class with Brand and Model.
#Create Car (Fuel Type) and Bike (Engine Capacity) child classes.
#Override display() in child classes.


class vehicle:
    brand="Tata"
    model="Nexon"

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)

class car(vehicle):
    fuel="Petrol"
    def display(self):
        print("\n\t\t\t\tCAR DETAILS")
        print("Brand",self.brand)
        print("Model",self.model)
        print("Fuel Type",self.fuel)


class bike(vehicle):
    engine=350
    def display(self):
        print("\n\t\t\t\tBIKE DETAILS")
        print("Brand",self.brand)
        print("Model",self.model)
        print("Engine Capacity",self.engine,"CC")

while True:
    print("\n\n\t\t\tVEHICLE MANAGEMENT SYSTEM\n\n")
    print("\n1 Car")
    print("\n2 Bike")
    print("\n3 Exit")
    ch=int(input("Enter choice you want to enter"))

    if ch==1:
        c=car()
        c.display()

    elif ch==2:
        b=bike()
        b.display()

    elif ch==3:
        print("Thank you")
        break

    else:
        print("Invalid choice")
'''


#Q12. Online Shopping System
#Create abstract Product class with private Product ID and Price.
#Child classes: Electronics (10%), Clothing (20%), Grocery (5%).
#Implement inheritance, encapsulation, abstraction and polymorphism.

from abc import ABC,abstractmethod

class Product(ABC):
    product_id=101
    price=1000

    @abstractmethod
    def display(self):
        pass

class electronics(Product):
    def display(self):
        print("\n\t\t\tELECTRONICS")
        print("Product ID:",Product.product_id)
        print("Product Price:",Product.price)
        print("Final Price:",Product.price-(Product.price*10/100))

class clothing(Product):
    def display(self):
        print("\n\t\t\tCLOTHING")
        print("Product ID:",Product.product_id)
        print("Product Price:",Product.price)
        print("Final Price:",Product.price-(Product.price*20/100))
class grocery(Product):
    def display(self):
        print("\n\t\t\tGROCERY")
        print("Product ID:",Product.product_id)
        print("Product Price:",Product.price)
        print("Final Price:",Product.price-(Product.price*30/100))


while True:
    print("\n\n\t\t\tONLINE SHOPPING SYSTEM\n\n")
    print("\n1 Electronics")
    print("\n2 Clothing")
    print("\n3 Grocery")
    print("\n4 Exit")
    ch=int(input("Enter your choice"))

    if ch==1:
        e=electronics()
        e.display()
    elif ch==2:
        e=clothing()
        e.display()
    elif ch==3:
        e=grocery()
        e.display()
    elif ch==4:
        print("Thank you")
        break
    else:
        print("Invaid choice")
