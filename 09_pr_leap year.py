y=int(input("\nEnter a year : "))
if y%100==0:
    if y%400==0:
        print(f"\nThe year {y} is a leap year.\n")
    else:
        print(f"\nThe year {y} is not a leap year.\n")
else:
    if y%4==0:
        print(f"\nThe year {y} is a leap year.\n")
    else:
        print(f"\nThe year {y} is not a leap year.\n")