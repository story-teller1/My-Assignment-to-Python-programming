n=int(input("\nEnter any number : "))
while n<0:
    n=int(input("Invalid input!\nEnter any valid natural number : "))
l=[]
if n>=0 :
    l.append(0)
if n>=1:
    l.append(1)

    for i in range(n-2):
        c=l[i]+l[i+1]
        l.append(c)
print(l)
print(l[-1])
