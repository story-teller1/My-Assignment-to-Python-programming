n1=eval(input("\nEnter the 1st number : "))
n2=eval(input("Enter the 2nd number : "))
n3=eval(input("Enter the 3rd number : "))
if n1>n2:
    n=n1
    s=n2
else:
    n=n2
    s=n1
if n>n3:
    print(f"\nThe greatest number among the numbers {n1}, {n2} and {n3} is {n}")
    if s>n3:
        print(f"The smallest number among the numbers {n1}, {n2} and {n3} is {n3}\n")
    else:
        print(f"The smallest number among the numbers {n1}, {n2} and {n3} is {s}\n")
    
else:
    print(f"\nThe greatest number among the numbers {n1}, {n2} and {n3} is {n3}")
    print(f"The smallest number among the numbers {n1}, {n2} and {n3} is {s}\n")