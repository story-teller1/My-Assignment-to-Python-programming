try:
    #inputs a number from the user
    n=int(input("\nEnter a number : "))
    
    #defining  variables to store the given number and the sum of the digits respectively
    n1=n
    sum=0
    
    #calculating the sum of the digits
    while n>0:
        r=n%10
        sum+=r
        n=n//10
        
        
    #printing the results
    print(f"\nThe sum of the digits of the number {n1} is : {sum}\n")
    
except:
    #handling the program from the invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
