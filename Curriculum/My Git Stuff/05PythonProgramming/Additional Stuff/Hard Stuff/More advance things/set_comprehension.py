# Set comprehension

nums = [1, 1, 2, 1, 3, 9, 4, 5, 5, 6, 7, 7, 8, 9, 10]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)
# curly braces tells python want a set not a list
my_set = {n for n in nums}
print(my_set)