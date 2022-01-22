n=int(input("\nEnter the number up to which number of line you want to print the pattern : "))
print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
      
        print(j,end="")
    print()
print()