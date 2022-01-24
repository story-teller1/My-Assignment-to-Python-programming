#input a number from user
n=int(input("\nEnter any number : "))


#makes sure that the inputted number is positive
while n<0:
        n=int(input("\nInvalid input!\nEnter any natural number : "))
        
#defining a new variable i
i=0
#finding the order of the number 
while i<n:
    if n//10**i==0:
        order=i
        
        break
    i+=1
#finding the sum of the digits raised to its order

sum = 0

c = n
while c > 0:
   digit = c % 10
   sum += digit ** order
   c //= 10

#concluding whether it's an Armstrong number or not
if n == sum:
   print(f"\n{n} is an Armstrong number.\n")
else:
   print(f"\n{n} is not an Armstrong number.\n")
