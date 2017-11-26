# PROBLEM : Receive miles and convert to kilometers

#       kilometers = miles * 1.60934
#       Enter Miles 5
#       5 miles equals 8.04 kilometers (paradigma)


# ask the user to put number of miles and assign them to miles variable

miles = input('PUT MILES: ')

# convert string miles to Integer miles

miles = int(miles)

# perform maths

kilometers = miles * 1.60934

# print results using format()

print ("{} miles equal {} kilometers".format(miles, kilometers))




