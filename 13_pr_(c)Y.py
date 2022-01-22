# from cgi import print_environ


n=int(input("\nEnter any number up to which number of line you want to print the letter : "))

print("\nHere is your required letter.\n")

if n%2!=0: 
    for i in range(n//2):
        print(" "*i+"*"+" "*(n-2-2*i)+"*")   
    for i in range(n//2+1):
        print(" "*(n//2)+"*")
else:
    m=n+1
    for i in range(m//2):
        print(" "*i+"*"+" "*(m-2-2*i)+"*")   
    for i in range(m//2):
        print(" "*(m//2)+"*")