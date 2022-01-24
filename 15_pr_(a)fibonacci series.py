try:
    #inputs a number from the user
    n=int(input("\nEnter any number : "))
    
    #makes sure that the given number is not less than zero
    while n<0:
        n=int(input("Invalid input!\nEnter any valid natural number : "))
    
    #creates an empty list
    l=[]
    
    #filling up the list with fibonacci numbers
    if n>=0 :
        l.append(0)
    if n>=1:
        l.append(1)
    
        for i in range(n-2):
            c=l[i]+l[i+1]
            l.append(c)
            
    #printing the fibonacci series
    print(f"\nThe required fibonacci series is as follows:\n{l}")
    print(f"\nThe required fibonacci number is {l[-1]}")

except:
    #handling the program from the invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
