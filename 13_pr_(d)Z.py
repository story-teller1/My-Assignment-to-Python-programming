n=int(input("\nEnter any number up to which number of line you want to print the letter : "))

print("\nHere is your required letter.\n")

for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        c= (" "*(n-i))+"*"
        print(c)
