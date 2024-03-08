stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip(" "" ")

# Type your code below
E_notation = stdform.replace("x10^", "E")
Exponent_pos = stdform.find("^")
Exponent = stdform[Exponent_pos+1:]
Mantissa_pos = stdform.find("x")
Mantissa = stdform[:Mantissa_pos]

print(Exponent)
print(Mantissa)
print("This number is in E notation is " +  E_notation) 