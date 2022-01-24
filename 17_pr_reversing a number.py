n=int(input("\nEnter a number : "))
n1=n
reverse_n=0
while n>0:
    r=n%10
    reverse_n=reverse_n*10 + r
    n=n//10

print(f"\nThe reverse of the digits of the number {n1} is : {reverse_n}\n")