emptyTuple = ()
print(emptyTuple)

singleton = 'hello'
print(singleton)

tup = 'hello', 'world', 'area' , 51, 2343.2
print(tup) #('hello', 'world', 'area', 51, 2343.2)
print(tup[2]) # fetch tuple value "area" using index
x, y, z, a, b = tup # unpacking tuple into variables
print(a)