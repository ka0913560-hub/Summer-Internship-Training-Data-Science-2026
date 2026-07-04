#Data Science DAY 2

'''
#Q1) TO PRINT TABLE OF 2 WITH HELP OF FOR LOOP

for i in range(1,11):
    print("2 x",i,"=",2*i)
'''

'''
#Q2) TO PRINT NO OF EVEN NUMBERS BETWEEN 1 TO 100 & also find their sum
print("All even n umbers between 1 to 100 are:\n\n",)
for i in range(1,101):
    if(i%2==0):
        print(i)
        c=0
        for i in range(c,i+1):
            c=c+i
print("\n\nSum of all even numbers between 1 to 100=",c)


print("All odd umbers between 1 to 100 are:\n\n",)        
for i in range(1,101,2):
    print(i)
'''

'''
#Q3) Prepare a grade system in which students with marks
#80 to 100 A
#79 TO 60 B
#59 TO 50 C
# ELSE FAil

print("\t\tGRADE SYSTEM\t\t")
m=int(input("Enter your marks"))

if(80<=m<=100):
    print("YOUR GRADE IS A")
elif(60<=m<=79):
    print("YOUR GRADE IS B")
elif(50<=m<=59):
    print("YOUR GRADE IS C")
elif(m<50):
    print("YOUR GRADE IS F")
else:
    print("Invalid Choice")
    
'''

'''
#Q4) find factorial of 5
n=int(input("Enter number"))
fact=1
for i in range(fact,n+1):
    fact=fact*i
print(fact)

'''

'''
#Q5) FIND THE LARGEST NUMBER FROM 20,21,70,80,64,36
L=[20,21,70,80,64,36]

#l=[]
#n=int(input("How many numbers do you want to enter"))
#for i in range(n):
#    num=int(input("Enter number:"))
#    L.append(n)

l=L[0]
s=L[0]
for i in range(1,len(L)):
    s=s+L[i]
    if(L[i]>l):
       l=L[i]
    
print("Largest number among 6 no is=",l)
print("Sum is",s)
print("Average is=",s/len(L))


#same ques using max and sum function
l=max(L)
s=sum(L)

print("Largest number=",l)
print(s)
'''

'''
#q6) Print star pattern
# *
# **
# ***
# ****
# *****
# ******

for  i in range(1,7):
    print(i*"*")

#  same pattern in reverse order
for  i in range(1,7):
    print((7-i)*"*")


'''

'''
#Q7) Print star pattern
#  *
# **
#***
#   ***
#    **
#     *

c=" " 
for  i in range(1,4):
    print((c*(3-i))+i*"*")

for  i in range(1,4):
    print((c*(2+i))+(4-i)*"*")

'''

'''
#Q8) PRINT STAR PATTERN
#    *
#   ***
#  *****
# *******
c=" "
for i in range(1,5):
        print((c*(4-i))+("*"*(2*i-1)))
'''

'''
#Q) PRINT STAR PATTERN
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *

c=' '
for i in range(1,5):
    print(((4-i)*c)+(((2*i)-1)*"*"))
for i in range(5,0,-2):
    print((((5-i+2)//2)*c)+(i*"*"))
'''


#Q9) PRINT STAR PATTERN
#*
#**
#***
#****
#*****
#******
#*****
#****
#***
#**
#*

for  i in range(1,7):
    print(i*"*")

for  i in range(1,6):
    print((6-i)*"*")
