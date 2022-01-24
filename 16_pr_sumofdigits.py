n=int(input("\nEnter a number : "))
n1=n
sum=0
while n>0:
    r=n%10
    sum+=r
    n=n//10

print(f"\nThe sum of the digits of the number {n1} is : {sum}\n")