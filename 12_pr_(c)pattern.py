#inputs a number from the user up to which number of line he or she wants to print the pattern
n=int(input("\nEnter the number up to which number of line you want to print the pattern : "))
print()

#printing the pattern
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1)+" ")
    
   
print()
