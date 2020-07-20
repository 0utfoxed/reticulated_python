# Create a "float" object (a decimal number) named weight that holds the value 0.2, and create a string object named animal that holds the value "newt", then use these objects to print the following line without using the format() string method: 0.2 kg is the weight of the newt.

weight = 0.2

animal = "newt"

print(f"{weight} kg is the weight of the {animal}.")

# Display the same line using format() and empty {} place-holders

print("{} kg is the weight of the {}.".format(weight, animal))

# Display the same line using {} place-holders that use the index numbers of the inputs provided to the format() method

print("{1} kg is the weight of the {0}.".format(animal, weight))

# Display the same line by creating new string and float objects inside of the format() method

print("{kg_weight} kg is the weight of the {new_animal}.".format(kg_weight = 0.2, new_animal = "newt"))
