# if age is 5 Go to Kindergarten

age = eval(input("Enter age: "))

if age == 5:
    print("go to kindergarten")

#if age is <5

elif age < 5:
    print("sorry to young")

# ages 6 through 17 goes to grades 1 through 12

elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} Grade".format(grade))

# if age is greater then 17 say go to college
else:
    print("GO TO COLLEGE")

# try to complete with 10 or less lines
