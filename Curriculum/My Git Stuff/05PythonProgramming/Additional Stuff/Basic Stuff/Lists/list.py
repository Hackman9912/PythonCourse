# list syntax of even numbers

#even_numbers = [2, 4, 6, 8, 10]


# Lists can hold different types
#different_types_list = ['Chunn', 100, False, 3.14]

# show items in list
#print(different_types_list)

# using range in a list
#range_list = list(range(5))
#print(range_list)

# repetition operator
# list * n

names = ['Hydrick', 'George', 'Ali', 'Howard']
names = names[0] * 5

print(names)

# print numbers list multiple times
numbers = [1, 2, 3]*3

print(numbers)

# loop over list and display

large_numbers = [99, 100, 101, 2000000]
for n in large_numbers:
    print(n)


# indexing with lists
my_list = [10, 20, 30, 40, 50]
print(my_list[2])

# find length of list
len_list = len(my_list)
print(len_list)


# lists are mutable
large_numbers[1] = 1337
print(large_numbers)

