#Data Science Day 3

'''
Topic 1 Datasets
 i)List
ii) Tuple
iii) Dictonary
iv) Set

'''



'''
#Q1) to use differnt datatypes using worlcups eg


worldcup={
    2021:{"Teams":["India","Australia","Pakistan","England"],
          "captains":{"India":"Virat Kohli","Australia":"Aaron Finch","England":"Eoin Morgan","Pakistan":"Babar Azam"},
          "Total players":{"India":15,"Australia":15,"England":15,"Pakistan":15},
          "winner":"India"
          },
    2027:{"Teams":["India","Australia","England","South Africa"],
          "captains":{"India":"Rohit Sharma","Australia":"Pat Cummins","England":"Jos Buttler","South Africa":"Temba Bavuma"},
          "Total players":{"India":15,"Australia":15,"England":15,"South Africa":15},
          "winner":"To be decided"
          }
    }

#year=int(input("Enter world cup year:"))

while True:
    print("\t\t\t\t\n\nWORLD CUP\t\t\t")
    print("\n1 Show Years")
    print("\n2 Show Teams")
    print("\n3 Show Captain")
    print("\n4 Show Winner")
    print("\n5 Show Total Players")
    print("\n6 Exit")

    ch=int(input("Enter choice; "))

    if ch==1:
        print("Availabe years:",list(worldcup.keys()))

    elif ch==2:
        year=int(input("Enter worldcup year"))
        print("Teams",worldcup[year]["Teams"])

    elif ch==3:
        year=int(input("Enter worldcup year"))
        team=input("Enter Team name: ")
        print("Captains",worldcup[year]["captains"][team])

    elif ch==4:
        year=int(input("Enter worldcup year"))
        print("winner:",worldcup[year]["winner"])

    elif ch==5:
        year=int(input("Enter worldcup year"))
        team=input("Enter Team name: ")
        print("Total Players",worldcup[year]["Total players"][team])

    elif ch==6:
        print("Thank you")
        break
    else:
        print("Invalid choice")

'''



#ATM MANAGEMENT SYSTEM
#LANGUAGE CHECK
#THEN FOUR OPTIONS
#i) cash withdrawl
#ii) balace check
#iii) password change
#iv) help

atm={
    "Language":["English","Hindi"],
    "Password":"1234",
    "Balance":50000
    }

print("\n\t\t\t\tATM MANAGEMENT SYSTEM")
print("Select language")
print("1 English")
print("2 Hindi")

lang=int(input("Enter choice:"))

while True:
    print("\n1Cash withdrawal")
    print("\n2 Balance check")
    print("\n3 Password change")
    print("\n4 Help")
    print("\n5 Exit")

    ch=int(input("Enter choice"))
    if ch==1:
        amt=int(input("Enter Amount"))
        if amt<= atm['Balance']:
            atm['Balance']=atm['Balance']-amt
            print("Please collect your cash")
            print("Remaining balance=",atm['Balance'])
        else:
            print("Insufficient balance")

    elif ch==2:
        pwd=input("Enter password")
        if pwd==atm['Password']:
            print("Available Balance",atm['Balance'])
        else:
            print("Wrong Password")

    elif ch==3:
        old=input("Enter old password")
        if old==atm['Password']:
             new=input("Enter new passowrd")
             atm['Password']=new
             print("Password changed successfully")
        else:
            print("wrong password")

    elif ch==4:
        print("Contact customer care: 1800-123-456")

    elif ch==5:
        print("Thank You for using ATM")
        break
    else:
        ("Invalid choice")
