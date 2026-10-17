
weight=float(input("Enter your weight"))
unit=input("What you want to convert kilogram or pounds? (K or L)")

if unit=="K":
    weight=weight * 2.205
    unit= "Lbs."
elif unit=="L":
    weight=weight / 2.205
    unit= "Kgs."
else:
    print(f"{unit} is not valid!")

print(f"Your weight is:  {round(weight,3)} {unit}")