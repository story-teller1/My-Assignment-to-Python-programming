try:
    
    #inputs a number from the user
    n=eval(input("\nEnter any number : "))
    
    #defining a variable to check whether the number is prime or not
    prime= True
    
    #making sure that the given number is positive
    while n<=0:
        n=eval(input("\nInvalid input!\nEnter any natural number : "))
        
    #conditions for being prime
    if n>0:
        for i in range(2,n):
            if n%i==0:
               prime= False
               break
      
    #checking whether the number fulfils the condition
        if prime:
            print(f"\n{n} is a prime number.\n")

        else:
            print(f"\n{n} is not a prime number.\n")
    
            
    
except:
    #handling the program from the invalid inputs by the user
    print("\nPlease enter a numerical value.\n")

    
