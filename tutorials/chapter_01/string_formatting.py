first_name = "prince"
last_name = "thomas"
age = 19
full_name = first_name + " " + last_name

# Hey! I am prince thomas. I am 19 years old.

# Concatenation
print( "hey I am " + full_name + ". I AM " + str(age))

#.format() method
print("Hey! I am {} {}. I am {} years old.".format(first_name, last_name, age))

# f string method
print(f"Hey! I am {first_name} {last_name}. I am {age} years old.")


# Conversion of data types
# a = "19"
# print(int(a))
# print(float(a))