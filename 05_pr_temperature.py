try:
#inputs a temperature in degree Celsius from the user
  C=eval(input("\nEnter the temperature in degree Celsius : "))

#converting the temperature in degree Fahrenheit from Celsius
  F=9*C/5+32

#printing the results
  print(f"\n{C}°C is equal to {F}°F \nWhere C=Celsius & F=Fahrenheit.\n")

except:
  #handling the program from the invalid inputs by the user
  print("\nInvalid input!\nPlease enter a numeric value.\n")
