#inputs a year from the user
y=int(input("\nEnter a year : "))

#checks the century years whether it is a leap year or not
if y%100==0:
    if y%400==0:
        print(f"\nThe year {y} is a leap year.\n")
    else:
        print(f"\nThe year {y} is not a leap year.\n")
        
#checks the years other than the century years whether it's a leap year or not
else:
    if y%4==0:
        print(f"\nThe year {y} is a leap year.\n")
    else:
        print(f"\nThe year {y} is not a leap year.\n")
