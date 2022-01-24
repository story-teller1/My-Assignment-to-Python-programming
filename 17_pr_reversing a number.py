try:
    #inputs a number from the user
    n=int(input("\nEnter a number : "))
    
    #defining a variable to store the value of the given number and the reversed number
    n1=n
    reverse_n=0
    
    #calculation of the reversed number
    while n>0:
        r=n%10
        reverse_n=reverse_n*10 + r
        n=n//10

    #printing the results
    print(f"\nThe reverse of the digits of the number {n1} is : {reverse_n}\n")
    
except:
    #handling the program from the invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
