# Dictionaries iteration
print('Dictionaries iteration')
user = {
    "username": "tombombadil",
    "first_name": "tom",
    "last_name": "bombadil",
}
for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value.capitalize()}")
    print("------------------")

# Set iteration
directions = {'north', 'south', 'east', 'west'}
print(directions)
print(type(directions))
directions1 = set(['north', 'south', 'east', 'west'])
print(directions1)
print(type(directions1))
# making set from above comment till this line is same, i was just testing this concept

print('Set iteration')
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)

# Here is how you would iterate over a set. It is much like for a list. However, remember that the order may not remain static.
# You could also use range() and len() to get index values.
for direction in range(len(directions)):
    print(direction)