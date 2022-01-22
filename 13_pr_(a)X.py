n=int(input("\nEnter any odd number up to which number of line you want to print the letter : "))
print()
while n%2==0:
    
    m=int(input("Please enter an odd number as the letter which you want strongly requires odd number of lines.\nEnter any odd number here : "))
    n=m
    print()
   
print("\nThe required letter is given below: \n")


for i in range(n//2+1):
    if i==n//2:
        print(" "*(i)+"*"+" "*(n-2-2*i))
        
    else:
        print(" "*i+"*"+" "*(n-2-2*i)+"*")
for i in range(n//2):
    print(" "*(n//2-i-1)+"*"+" "*(2*i+1)+"*")