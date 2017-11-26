# enter Calculation: 5 * 6
# 5 * 6 = 30

# store the user input in 2 numbers and the operator

num1, operator, num2 = input("ENTER THE NUMBERS AND OPERATOR : ").split() #<--- axristo split (error, giati thelei kena px. 5 + 5 )


# convert strings into integers

num1 = int(num1)
num2 = int(num2)


# if + then we need to provide output based on on addition + print

if operator == "+":
        print("{} + {} = {}".format(num1, num2, num1+num2))

elif operator == "-":
        print("{} - {} = {}".format(num1, num2, num1-num2))

elif operator == "*":
        print("{} * {} = {}".format(num1, num2, num1*num2))

elif operator == "/":
        print("{} / {} = {}".format(num1, num2, num1/num2))

else:
        print("USE EITHER + - * / NEXT TIME")

# you can also check is the value is >, <, >=, <=, != (!= non equal to)