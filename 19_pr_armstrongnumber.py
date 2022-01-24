n=int(input("\nEnter any number : "))
while n<0:
        n=int(input("\nInvalid input!\nEnter any natural number : "))
i=0
while i<n:
    if n//10**i==0:
        order=i
        
        break
    i+=1
sum = 0

c = n
while c > 0:
   digit = c % 10
   sum += digit ** order
   c //= 10
if n == sum:
   print(f"\n{n} is an Armstrong number.\n")
else:
   print(f"\n{n} is not an Armstrong number.\n")