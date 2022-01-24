try:
#inputs the length & breadth of the rectangle from the user
  l=eval(input("Enter the length of the rectangle : "))
  b=eval(input("Enter the breadth of the rectangle : "))


#finding the area of the rectangle
  a=l*b

#finding the perimetre of the rectangle
  p=(l+b)*2

#printing the results
  print(f"The area of the rectangle is {a}")
  print(f"The perimeter of the rectangle is {p}")

except:
  #handling the program from invalid inputs
  print("Invalid input!\nPlease enter a numeric value.")
 
