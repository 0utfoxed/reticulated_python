# Practice with the input() method

# user_input = input("Hey, what's up? ")

# print("You said: ", user_input)

response = input("What should I shout? ")

print("Well, if you insist...", response.upper())

print("The stored value of \"response\" is ", response)

response = response.upper()

print("Well, if you insist...", response)

print("The stored value of \"response\" is now ", response)

# Another way to get the same output as above is shown below. The one difference, here, is that the .upper() method is called, then used to assign the value to a new string of the same name. In the previous version, the upper method is combined with print() to display the uppercase version on the string while continuing to store the original input. This is demonstrated by the sequential print() statements included here.
