stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
mantissa , exponent = stdform.split("x10^")

print(f"This number in E notation is {mantissa}E{exponent}.")