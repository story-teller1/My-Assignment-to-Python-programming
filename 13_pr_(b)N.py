from cgi import print_environ


n=int(input("\nEnter any number up to which number of line you want to print the letter : "))
print("\nHere is your required letter.\n")
for i in range(n+1):
    print("*"+" "*(i)+ "*"  +" "*(n-i)+"*")