# Sets
# A set contains a collection of unique values and works like a mathematical set
# 1 All the elements in a set must be unique. No two elements can have the same value
# 2 Sets are unordered, which means that the elements are not stored in any particular order
# 3 The elements that are stored in a set can be of different data types

# Creating a set

my_set = set(['a', 'b', 'c'])
print(my_set)

my_set2 = set('abc')
print(my_set2)

# will remove the duplicates for us
my_set3 = set('aabbcc')
print(my_set3)

# will error, set can only take one argument
# my_set4 = set('one', 'two', 'three')
# print(my_set4)

# Brackets help
my_set5 = set(['one', 'two', 'three'])
print(my_set5)

# find length
print(len(my_set5))

# add and remove elements of a set
# initialize a blank set
new_set = set()
new_set.add(1)
new_set.add(2)
new_set.add(3)
print("New set", new_set)

# Update works
new_set.update([4, 5, 6])
print("After update: ", new_set)
new_set2 = set([7, 8, 9])
new_set.update(new_set2)
print(new_set)

# cannot do 10 instead would use .discard discard will do nothing if it won't work as opposed to return an error
new_set.remove(1)
print(new_set)

# using a for loop to iterate over a set
new_set3 = set(['a', 'b', 'c'])

for val in new_set3:
    print(val)

# using in and not operator to test the value of a set
numbers_set = set([1, 2, 4])
if 1 in numbers_set:
    print('The value 1 is in the set. ')

if 99 not in numbers_set:
    print('The value 99 is not in the set. ')

# Find the union of sets
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1.union(set2)
print('set3', set3)
# the same as above
set5 = set1 | set2
print('set5', set5)

# Find the intersection of sets
set4 = set1.intersection(set2)
print('set 4', set4)
# same as above
set6 = set1 & set2
print('set6', set6)

char_set = set(['abc'])
char_set_upper = set(['ABC'])

char_intersect = char_set.intersection(char_set_upper)
print('character intersect upper and lower', char_intersect)

char_union = char_set.union(char_set_upper)
print('character union upper lower', char_union)

# find the difference of sets
set7 = set1.difference(set2)
print('1 and 2 diff', set7)
print('set 1', set1)
print('set 2', set2)

set8 = set2.difference(set1)
print('set 8', set8)

set9 = set1 - set2
print('set9', set9)

# finding symmetric difference in sets
set10 = set1.symmetric_difference(set2)
print('set10', set10)

set11 = set1 ^ set2
print('set11', set11)

# find the subsets and supersets
set12 = set([1,2,3,4])
set13 = set([1,2])
print(' is 13 a subset of 12', set13.issubset(set12))

print('is 12 a superset of 13', set12.issuperset(set13))
