try:
# Finding the fibonacci number using while loop
    n=int(input("\nEnter any value : "))
    
# if the user inputs mistakenly a negative value, this will handle that
    while n<0:
        n=int(input("Invalid input!\nEnter any valid natural number : "))
        print()
        
    #defining two variable for finding the required fibonacci number
    a=0
    b=1
    print("\nThe required fibonacci number is  : \n")
    
# condition of a fibonacci number
    if n==0:
        print (f"{a}\n")
    elif n==1:
        print(f"{b}\n")
        
        
    else:
    # while the above 2 values are counted in the fibonacci series, i.e.,0 & 1 so, the loop will continue to n-2 terms.
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        print(f"{b}\n")
        
except:
    #handling the program from the invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
