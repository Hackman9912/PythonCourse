# enumerate()
# A way to go through an iterable and return the index of the object and the object
# iterates over different types of iterable objects and returns bothe the index and the also the value of each item.

# enumerate over some names
names = ['Daniesl', 'Joe', 'Jim', 'Travis']
# start will tell enumerate to start indexing wherever you tell it. Will also work if you do not add start
# print(list(enumerate(names, start = 4)))

# for name in enumerate(names):
#     print(name)
# displays it as 2 different variables and not as a tuple
# for count, item in enumerate(names, 1):
#     print(f'Count: {count}, Item:  {item}')

my_string = 'Enumerating is Powerful'

# for idx, ch in enumerate(my_string):
#     print(f'Index is {idx}, and character is {ch}')

# type cast to dictionaries

my_dict = {k : v for k , v in enumerate(names)}
print(my_dict)

