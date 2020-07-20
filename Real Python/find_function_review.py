# In one line, display the result of trying to find() the substring "a" in the string "AAA"; the result should be -1

print("AAA".find("a"))

# Create a string object that contains the value "version 2.0"; find() the first occurrence of the number 2.0 inside of this string by first creating a "float" object that stores the value 2.0 as a floating-point number, then converting that object to a string using the str() function

str_obj = "version 2.0"

float_number = 2.0

print(str_obj.find(str(float_number)))

# Write and test a script that accepts user input using input() , then displays the result of trying to find() a particular letter in that input

user_input = input("Input test data: ")

search_string = input("Search for: ")

if user_input.find(search_string) < 0:
	print("I'm sorry--your search term could not be found.")
else:
	print(f"Your search term was found at {user_input.find(search_string)}.")
