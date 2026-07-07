# Example 1
age = input("Enter your age: ")
age = int(age)
height = input("Enter your height: ")
height = float(height)
print("You are " + str(age) + " years old and " + str(height) + " feet tall.")

# Example 2 `wrong`
weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
Bmi = weight / (height * height)
print("Your BMI is: " , format(Bmi, '.2f'))

# Example 3
celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit is " , format(fahrenheit, '.2f'))
