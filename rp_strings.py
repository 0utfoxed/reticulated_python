# All of these are strings:
	
phrase = "Hello, world."
my_string = "We're #1!"
string_number = "1234"
conversation = 'I said, "Put it over by the llama."'

# It is possible to write a string across multiple lines in such a way that it still appears on a single line once run. To do this, we can "escape" the new line "character" by preceding it with a backslash. This technique is generalizable to most other symbols that you don't want to be handled in the typical way (e.g. quotation marks).

my_long_string = "Here's a string that I want to \ write across multiple lines, since it is long."

# Of note, it appears that this functionality is not actually available in Pythonista, as it wraps text by default. I also might be making some sort of mistake.

my_long_string = "Here's a string that I want to \
write across multiple lines since it is long."

print(my_long_string)

# Update: this feature _does_ actually work in Python; however, there appears to be a bug in syntax highlighting that prevents it from recognizing subsequent lines as part of a string.

# As another reminder, dashes _cannot_ be utilized in Python names, as they call the subtraction method.

my_string = "abc"

print(len(my_string))

# Strings can be "added" (i.e. concatenated) together in a manner not dissimilar to numbers, e.g.

string1 = "abra"
string2 = "cadabra"

concat_string = string1 + string2

print(concat_string)

# The result above can also be achieved in this way:
	
print("abra"+"ca"+"dabra")

# To combine numerous strings in the same line, with the addition of automatically inserted spaces, the following syntax can be employed:

print("Method 1")
print(string1, string2)

print("Method 2")
print("abra", "ca", "dabra")

# Strings in python are enumerated ("indexed") by default; values stored in these indexes can be accessed using square brackets appended to the string (or string-containing variable) of interest, e.g.

flavor = "birthday cake"
print(flavor[3])

# Note: Python indexation begins at ZERO.

# Index numbers are also referred to as "subscript" numbers.

# Index slicing can also be used to specify a _range_ of characters from a particular string, e.g.

print(flavor[:5])
print("birth")
print(flavor[5:])
print("day cake")
print(flavor[:])
print("birthday cake")

# Remember: when utilizing colon-defined ranges to slice out sections of a string, the second number (i.e. the number _after_ the colon) is _non-inclusive_.

''' Aside: On the "Immutability" of Strings in Python

Python strings are "immutable": once created, they cannot be changed.

The functional import of this fact is that, to alter a string, a new string must be created.

As an example, while the following code won't work:
	my_string = "goal"
	my_string[0] = "f"

The desired result could be achieved in this manner:
	my_string = "goal"
	my_string = "f" + my_string[1:]
'''

# Review exercise: print zing using characters from the word 'bazinga'

marble = "bazinga"

statue = marble[2:6]

print(statue)

print(statue)
 

