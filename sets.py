breakfast = {'bacon', 'egg', 'spam', 'spam', 'spam', 'spam', 'spam'}
print(breakfast)

# check if a value exist in a set
print('egg' in breakfast)

# add a single value in a set
breakfast.add('sausage')
print(breakfast)

# add multiple items as a list/set with update() both works
# breakfast.update({'Lobster Thermidor', 'truffle pate', 'crevettes', 'shallots','aubergines'})
breakfast.update(['Lobster Thermidor', 'truffle pate', 'crevettes', 'shallots','aubergines'])
print(breakfast)

# use discard to remove from a set
breakfast.discard('aubergines')
print(breakfast)

# ------------------------ Set operators -----------------------------------
print('Set operators')
hello = set("Hello")
world = set("World")
print(f"The unique letters in hello are: {hello}")
print(f"The letters in hello or world or both are: {hello|world}") # | is the symbol for union
print(f"The letters in both hello and world are: {hello&world}") # & is the symbol for intersection
print(f"The letters in hello but not world are: {hello-world}") # - is the symbol for difference
print(f"The letters in hello and world but not both are: {hello^world}") # ^ is the symbol for symmetric difference
