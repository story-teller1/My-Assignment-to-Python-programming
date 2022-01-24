# solving a quadratic equation
#instructing the user what to do, like how to enter all the required information, in which format etc
print("\nWe will solve a quadratic equation having this form : \n\t\tax^2 + bx + c = 0\nPlease Enter the required information below :")
a=eval(input("\nEnter the coefficient of x^2 (a) : "))
b=eval(input("Enter the coefficient of x   (b) : "))
c=eval(input("Enter the constant term      (c) : "))

#adjusting the '+' and the '-' sign of the coefficients & constant terms
if b>=0:
    p="+ "+str(b)
    if b==1:
        p="+ "
    
else:
    p="- "+str(-b)
    if b==-1:
        p="- "
if a==1:
        q=" "
elif a==-1:
    q="-"
if c>=0:
    r="+ "+str(c)
    if c==1:
        r="+ 1"
    
else:
    r="- "+str(-c)
    if c==-1:
        r="- 1"
        
#defining the discriminant of the quadratic equation
d=(b**2-4*a*c)

#checking whether the equation has real roots or not
if d<0:
    print("\nThis equation has no real roots.")
    
    
#if the equation has real roots then finds it and print them
else:
    x1=(-b+(d)**0.5)/(2*a)
    x2=(-b-(d)**0.5)/(2*a)
    print(f"\nThe required solutions of the equation \n\t  {q}x^2 {p}x {r} = 0\n are {x1} and {x2} respectively.")
    
