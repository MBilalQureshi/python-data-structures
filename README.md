# python-data-structures
python run.py
# javascript-data-structures
node app.js

Pythons list and JS array is actually same

## Some List/Array methods
Note that these may not be available in all languages and this list is not all-inclusive; it's just to give you an idea of what's possible:
- pop()	Pop the last item off the end of the list
- push()	Push a new item onto the end of the list
- slice()	Get a subset of the list (e.g. in a 10-item list, get items 3-6)
- shift()	Pop the first item out of the list and shift the others to the left
- unshift()	Push a new item onto the front of the list and shift the others to the right
- sort()	Sort the list in various ways
- len()/.length	Return the number of items in the list
- reverse()	Reverse the list

## Python - List
- ordered and is changeable.
- It can contain duplicate items
- items can be of different types such as strings, integers, floats or even another list.
- As a list is ordered, you can use an index to find an element in the list. Lists are zero-indexed, so the first element has index 0.
- you would choose a list data structure when you need an ordered sequence of items that you intend to be modified or appended.

### List Slicing & Indexing
See list.py for more understanding.

### Python - List Methods
As a list can contain many data types, not all methods will work on all lists
- list.append(x)	Add an item to the end of the list.
- list.extend(list)	Extend the list by appending another list.
- list.insert(i, x)	Insert an item at a given position. The first argument is the index of the element before which to insert
- list.remove(x)	Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
- list.pop(i)	Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
- list.clear()	Remove all items from the list.
- list.index(x, start, end)	Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation.
- list.count(x)	Return the number of times x appears in the list.
- list.sort(key=None, reverse=False)	Sort the items of the list in place
- list.reverse()	Reverse the elements of the list in place.
- list.copy()	Return a copy of the list. Equivalent to a[:].

## Python Tuples
- Unlike a list, it is not changeable
- It can contain duplicate items. 
- Those items can be of different types such as strings, integers, floats or even another tuple.
- Creating a tuple is referred to as packing. So when you want to get the values back, it is referred to as unpacking.
- It is also possible to get a value with indexing.
- So why choose a tuple over a list? As it is not changeable, it can be used where you have a constant set of values.
- Tuples are also more memory efficient

## Python Dictionaries
- You would choose a dictionary as a data structure when you have values you want to associate with a key.
- To delete a key/value pair use **del** and the key.
- To list the keys in the dictionary, you can use **list()** or **sorted()** 
- If you just want to know if a key exists within the dictionary, use the **in** keyword.
- The order of a dictionary is not fixed. Two people creating the same dictionary on different computers might get a different order of items. 
- It does not have an index as a list has.

### Getting & Setting Dictionary Items
- **dict()** function, which can create dictionaries **from lists**.
- The **fromkeys()** method is used to specify the keys list as the keys and a variable of an empty string as the values.
- To set a value, you can use the items key in square bracket notation and the assignment operator with a value. The default values are all overridden with the new values.
- If we attempted to get the value of a **nonexistent key**, then an error would occur. To avoid this you can use the **get()** method which will get the value if the key exists and return **None** if it does not.
- If we want to get a list of the keys only you can use the **keys()** method and wrap that in a **list()** function. The same syntax but using values or items will get a list of the dictionary values or items instead.
- See dict.py file to see this in action.