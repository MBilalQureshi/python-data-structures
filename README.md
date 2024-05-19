# python-data-structures
python run.py
# javascript-data-structures
node app.js

Pythons list and JS array is actually same

## Some List/Array methods
Note that these may not be available in all languages and this list is not all-inclusive; it's just to give you an idea of what's possible:
Method/Function	    Purpose
pop()	Pop the last item off the end of the list
push()	Push a new item onto the end of the list
slice()	Get a subset of the list (e.g. in a 10-item list, get items 3-6)
shift()	Pop the first item out of the list and shift the others to the left
unshift()	Push a new item onto the front of the list and shift the others to the right
sort()	Sort the list in various ways
len()/.length	Return the number of items in the list
reverse()	Reverse the list

## Python - List Methods
As a list can contain many data types, not all methods will work on all lists
Method	Description
list.append(x)	Add an item to the end of the list.
list.extend(list)	Extend the list by appending another list.
list.insert(i, x)	Insert an item at a given position. The first argument is the index of the element before which to insert
list.remove(x)	Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
list.pop(i)	Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
list.clear()	Remove all items from the list.
list.index(x, start, end)	Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation.
list.count(x)	Return the number of times x appears in the list.
list.sort(key=None, reverse=False)	Sort the items of the list in place
list.reverse()	Reverse the elements of the list in place.
list.copy()	Return a copy of the list. Equivalent to a[:].

## Python Tuples
Unlike a list, it is not changeable
It can contain duplicate items. 
Those items can be of different types such as strings, integers, floats or even another tuple.
Creating a tuple is referred to as packing. So when you want to get the values back, it is referred to as unpacking.
It is also possible to get a value with indexing.
So why choose a tuple over a list? As it is not changeable, it can be used where you have a constant set of values.
Tuples are also more memory efficient