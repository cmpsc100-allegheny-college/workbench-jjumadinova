fruit = ["apple", "banana", "orange", "apple", "strawberry"]

print(fruit)

# add an item to the list
fruit.append("pear")

print(fruit)

# get an index/position of an item in the list
print("index of apple: ", fruit.index("apple"))

# get a size of the list
print("number of elements in fruit: ", len(fruit))

# get the number of times an item appear in the list
print("count of apple: ", fruit.count("apple"))

# dictionaries
print("DICTIONARY EXAMPLES")

fruit_dict = {'apples': 4, 'bananas': 3, 'oranges': 2, 'strawberries': 10}
print(fruit_dict)

fruit_dict['pears'] = 6
print(fruit_dict)

fruit_dict['apples'] += 1
print(fruit_dict)

print(list(fruit_dict)) # list of keys

print(sorted(fruit_dict)) # sort the dict