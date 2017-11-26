# have the user enter their investment amount and expected interest rate is



investment_amount, interest_rate = input("ENTER YOUR INVESTMENT AMOUNT AN INTEREST RATE: ").split()

# each year their investment will increase by their investment + their investment * interest


# print out the earning after a 10 year period
investment_amount = float(investment_amount)

interest_rate = float(interest_rate) * .01

investment_increase = investment_amount + (investment_amount * interest_rate)

# ask for the money invested + the interest rate

# convert the value to a float

# convert value to a float and round the percentage rate by 2 digits

# cycle through 10 years using a for loop and range from 0 to 9

# output the results

investment_increase = float(investment_increase)

for i in range(10):
    print("INVESTMENT AFTER 10 YEAR:  {:.2f}".format((investment_increase * interest_rate) * i))



#(t exw peiraksei pl) vgale akri.