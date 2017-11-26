# we will provide different output based on age
# 1 - 18 -> important
# 21, 50, > 65 -> Important
# all others -> Not Important

# Receive age and store in age
age = eval(input("Enter age: "))                                #eval = automaticaly convert str to int

# and : If both are true it returns true
# or : If either condition is true then true
# not : Convert a true condition into a false

# if age is both greater than or equal to 1 and less than or equal to 18 Important

if (age >= 1) and (age <= 18):
    print("Important Birthday")


# if age is either 21 or 50 Important

elif (age == 21) or (age == 50):
    print("Important Birthday")

# we check if age is less than 65 and then convert True to False and vice versa

elif not(age < 65):
    print("Important Birthday")

# Else not Important

else:
    print("Sorry not Important Birthday")