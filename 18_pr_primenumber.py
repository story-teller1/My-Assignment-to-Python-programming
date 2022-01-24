try:
    n=eval(input("\nEnter any number : "))

    prime= True
    while n<0:
        n=eval(input("\nInvalid input!\nEnter any natural number : "))
    if n>0:
        for i in range(2,n):
            if n%i==0:
               prime= False
               break
        if prime:
            print(f"\n{n} is a prime number.\n")

        else:
            print(f"\n{n} is not a prime number.\n")
    
            
    
except:
    print("\nPlease enter a numerical value.\n")

    