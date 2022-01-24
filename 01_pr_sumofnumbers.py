try:
#inputs two numbers a & b from the user
  a =int(input("Enter the first value : "))
  b= int(input("Enter the second value : "))

#adds the two numbers
  c = a + b	

#printing the result
  print (f"The sum of {a} and {b} is {c}.")
except:
  #handles the program from invalid inputs from the user
  print ("Invalid input!\nPlease enter a numeric value.")
