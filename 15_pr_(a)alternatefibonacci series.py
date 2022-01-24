from asyncio.proactor_events import _ProactorWritePipeTransport
from os import sep

try:
    #inputs a number from the user
    n=int(input("\nEnter any value : "))
    
    #makes sure that the given number is not less than zero
    while n<0:
        n=int(input("Invalid input!\nEnter any valid natural number : "))
        print()
    a=0
    b=1
    print("\nThe required fibonacci series is as follows : \n")
    if n==0:
        print (a)
    elif n==1:
        print(a,b ,sep=",")
    else:
        for i in range(n+1):
            c=a+b
            print(a,end=",")
            a=b
            b=c
    print("\n")
    
except:
    #handling the program from the invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
