n1=int(input("\nEnter 1st number :  "))
n2=int(input("Enter 2nd number :  "))
c=0
if n1>=n2:
    n=n2
else:
    n=n1
for i in range(1,n//2+1):
        
    if n1%n2==0:
        c=n2
    elif n2%n1==0:
        c=n1
    else:
        if n1%i==0 and n2%i==0:

            c=i
print (f'\nThe Highest Common Factor of {n1} and {n2} is {c}.')
print (f'\nThe Lowest Common Multiple of {n1} and {n2} is {int(n1*n2/c)}.\n')