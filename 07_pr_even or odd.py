try:
#inputs a number from the user
    n=eval(input("\nEnter any number : "))

#checking the number whether it is even
    if n%2==0:
        print(f"\nThe given number {n} is even.\n")

#checking the number whether it is odd    
    else:
        print(f"\nThe given number {n} is odd.\n")

except:
    #handling the program from the invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
