n=int(input("\nEnter the number up to which number of line you want to print the pattern : "))
print()
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1)+" ")
    
   
print()