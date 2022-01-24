
try:
    #inputs two number from the user
    n1=int(input("\nEnter 1st number :  "))
    n2=int(input("Enter 2nd number :  "))
    
    #defining a variable to have the hcf & lcm
    c=0
    
    #checking which number is greater among the numbers given
    if n1>=n2:
        n=n2
    else:
        n=n1
    
    #determining the hcf
    for i in range(1,n//2+1):
        
        if n1%n2==0:
            c=n2
        elif n2%n1==0:
            c=n1
        else:
            if n1%i==0 and n2%i==0:

                c=i
                
    #printing the hcf & lcm of the two given numbers                        
    print (f'\nThe Highest Common Factor of {n1} and {n2} is {c}.')
    print (f'\nThe Lowest Common Multiple of {n1} and {n2} is {int(n1*n2/c)}.\n')
    
    
  except:
    #handling the program from invalid inputs
    print ("\nPlease enter valid numeric input")
