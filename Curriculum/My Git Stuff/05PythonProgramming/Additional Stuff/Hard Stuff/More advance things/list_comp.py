# list comprehension
# Good way to create a new list by performing an operation on each item in an existing list

# Separating letters in a string
# chars = []
# for ch in 'Daniel':
#     chars.append(ch)
# print(chars)

# chars2 = [ch for ch in 'Daniel']
# print(chars2)


# squares = [x*x for x in range(11)]
# print(squares)


# list of tuples
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# combined_list = [(x, y) for x in list1 for y in list2]
# print(combined_list)

# list comprehension with optional predicate
# evens = [x for x in range(21) if x % 2 == 0]
# print(evens)

# # list comprehension with multiple optional predicate
# numbers = [x for x in range(21) if x % 2 == 0 or x % 5 == 0]
# print(numbers)

# # if else list comprehension
# obj = [ 'Even' if i % 2 == 0 else 'Odd' for i in range(10)]
# print(obj)
# print('\n' * 50)
# # flatten a list
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = [num for row in matrix for num in row]
# print(flat_list)

nums = [1, 2, 3, 4]
str = ['a', 'b', 'c', 'd']
# # I want a (letter, number) pair for each letter in str and each number in nums

# my_list  = []
# for letter in str:
#     for num in nums:
#         my_list.append((letter, num))
# print(my_list)

my_list2 = [(letter, num) for letter in str for num in nums]
print(my_list2)