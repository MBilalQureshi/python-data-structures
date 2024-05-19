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