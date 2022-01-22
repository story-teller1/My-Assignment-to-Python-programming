n=int(input("\nEnter any odd number up to which number of line you want to print the pattern : "))
print()
while n%2==0:
    
    m=int(input("Please enter an odd number as the pattern which you want strongly requires odd number of lines.\nEnter any odd number here : "))
    n=m
    print()
   
print("\nThe required pattern is given below: \n")
    
for i in range(1,n//2+2):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(1,n//2+1):
    print(" "*(i+n//2)+"*"*(2*(n//2-i+1)-1))
    
   
print()