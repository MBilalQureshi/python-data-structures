# myMixedlist 
myMixedlist = [1,2,3,True,'hello', None,[1,2,3]]
print(myMixedlist)

# Looping through list
for item in myMixedlist:
    print(item)

# looping through only list inside list
for item in myMixedlist:
    if(type(item)==list):
        print(item)

# append older list in new empty one
newMixedList = []
for item in myMixedlist:
    newMixedList.append(item)
print(newMixedList)

# -------------- List Slicing and indexing ------------------
print('List indexing')
fruits = ["apple", "banana", "peach", "pear", "plum", "orange", "avacado","stawberries", "watermelon"]
print(fruits[0])
#  Using an index of -1 gives the last element. Negative indexing counts from the right
print(fruits[-1]) # orange
print('List Slicing - HINT: slice(start, end, step)')
sliceMe = slice(1,4,2)
print(fruits[sliceMe])
# This will get only first TWO item from the list
sliceSingle = slice(2)
print(fruits[sliceSingle])
# this will only remove the last item from the list
removeLast = slice(-1)
print(fruits[removeLast])
print('Use a SHORTEND slice notation rather than create a new slice object each time. The slice() object is still being used behind the scenes')
print('Hint Shorthand slicing  = start index, stop index , step')
print(fruits[0:2])
print(fruits[0:7:3])
print(f"Only END index is given{fruits[:3]}")
print(f"Only START index is given{fruits[5:]}")
print(f"Only STEP is given{fruits[::3]}")