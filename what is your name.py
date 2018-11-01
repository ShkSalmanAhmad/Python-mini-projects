# Ask user for name

name = input("What is your name?: ")


# Ask user for age

age = input("How old are you?: ")


# Ask user for city

city = input("What city do you live in?: ")



# Ask user for what they enjoy

leisure_time = input("What do you like to do during leisure time?: ")


# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name, age, city, leisure_time)

# Print output to screen

print(output)
