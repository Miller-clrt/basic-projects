user=input("Do you want to convert temperature to Fahrenheit or Celsius (F/C)")
temp=float(input("Enter the temperature: "))

if user == "F":
     temp=round((9*temp)/5+32,1)
     print(f"The temperature in Fahrenheit is: {temp}F")
elif user == "C":
    temp=round((temp-32)*5/9,1)
    print(f"The temperature in Celsius us: {temp}C")
else:
    print(f"{user} is invalid input for this program!")

