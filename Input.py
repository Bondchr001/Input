

# Print a welcome message
print("=== Temperature Converter ===")
print("Convert Celsius to Fahrenheit")
print()


c = (input("Enter a temperature Celsius: "))


# TODO: Convert the input string to a number
# Hint: Should you use int() or float()?
c = float(c)

# TODO: Calculate Fahrenheit
# Formula: F = C × 9/5 + 32
f = c * 1.8 + 32

# TODO: Display the result
# Show both the Celsius and Fahrenheit values
print(c, "degrees Celsius =", f , "degrees Fahrenheit")

print()
print("Thank you for using the Temperature Converter!")
