# Program to show the working of logical operators..

person = input("Enter Person name: ")
age = int(input("Enter Age: "))
weather = input("Enter Weather Conditions (Clear/Rainy/Stormy): ").strip().capitalize()


# logical and and logical or
if age >= 18 and (weather == "Clear" or weather == "Sunny"):
    print(f"{person} you can drive today, as weather is {weather}")
else:
     print(f"{person} you cannot drive today, as weather is {weather}")

# logical not
is_premium = False
has_license = True

if not is_premium:
     print("show ads as user is normal")

if not has_license:
     print("you cannot drive as you donot have license")
else:
     print("you can drive")