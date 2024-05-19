user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
# fetch value using key
print(user['age'])

# Adding new key value pairs
user['home'] = 'Withywindle, Middle-Earth'

# Updating already exisiting key
user['age'] = 99
print(user)

# deleteing a key/value pair
del user['home']
print(user)

# list all keys in dict
print(list[user])
# fetch sorted list of all keys from dict
print(sorted(user))
# use type to check the type, what is the type of sorted list conating keys of dict
print(type(sorted(user))) # <class 'list'>

# Check if key exist in dict
print('username' in user)

