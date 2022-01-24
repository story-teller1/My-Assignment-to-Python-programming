try:
  
#inputs three numbers from the user
  n1=eval(input("Enter the first decimal number : "))
  n2=eval(input("Enter the second decimal number : "))
  n3=eval(input("Enter the third decimal number : "))

#finding the sum of the numbers
  sum=n1+n2+n3

#finding the average of the numbers
  average=(n1+n2+n3)/3

#printing the results
  print(f"\nThe sum of the numbers {n1}, {n2} and {n3} is : {sum}")
  print(f"\nThe average of the numbers {n1}, {n2} and {n3} is : {average}\n")

except:
   #handling the program from invalid inputs by the user
    print("\nInvalid input!\nPlease enter a numeric value.\n")
