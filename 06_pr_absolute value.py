try:
#inputs a number from the user
    n=eval(input("\nEnter any number : "))

#finding the absolute value of the number
    if n>=0:
        print(f"\nThe absolute value of the given number {n} is : {n}\n")

    else:
        print(f"\nThe absolute value of the given number {n} is : {-n}\n")

except:
    #handling the program from the invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
