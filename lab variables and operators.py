# # Function to calculate multiplication and sum
def calculate(num1, num2):
    multiplication = num1 * num2
    summation = num1 + num2
    return multiplication, summation

# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculation
multiplication, summation = calculate(num1, num2)

# Display results
print(f"The multiplication of {num1} and {num2} is: {multiplication}")
print(f"The sum of {num1} and {num2} is: {summation}")
