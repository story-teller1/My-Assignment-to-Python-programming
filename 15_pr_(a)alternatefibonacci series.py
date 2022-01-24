from asyncio.proactor_events import _ProactorWritePipeTransport
from os import sep


n=int(input("\nEnter any value : "))
while n<0:
    n=int(input("Invalid input!\nEnter any valid natural number : "))
    print()
a=0
b=1
print("\nThe required fibonacci series is as follows : \n")
if n==0:
    print (a)
elif n==1:
    print(a,b ,sep=",")
else:
    for i in range(n+1):
        c=a+b
        print(a,end=",")
        a=b
        b=c
print("\n")