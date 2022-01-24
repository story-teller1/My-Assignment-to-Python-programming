#inputs a number from the user up to which line the user wants to print the pattern
n=int(input("\nEnter the number up to which number of line you want to print the pattern : "))
print()

#prints the required pattern
for i in range(1,n+1):
    print("*"*i)
print()
