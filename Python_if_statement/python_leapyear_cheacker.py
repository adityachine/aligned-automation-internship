yourname= input("Your Name Please...!:->")
print("Hii", yourname)
l_year =int(input("Please Enter Year that you want to check:->"))

divforyear= (l_year%4)

if divforyear == 0:
    print("yes it's a leap year",yourname,"Happy Leap year......!")
else:
    print("Sorry ",yourname,"it's not a leap year ")

