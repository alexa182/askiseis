# ask the user to import 2 values and store them in variables num1 num2
num1, num2 = input('ENTER 2 NUMBERS: ').split()

# convert the strings into regular numbers Integer

num1 = int(num1)
num2 = int(num2)

# add the values entered and store in sum

sum1 = num1 + num2

# subtract values and store in difference

difference = num1 - num2

# multiply the values and store in product

product = num1 * num2

# divine the values and store in quotient

quotient = num1 / num2

# use modules on the values to find the remainder

remainder = num1 % num2

# print the results

print("{} + {} = {}".format(num1, num2, sum1))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

