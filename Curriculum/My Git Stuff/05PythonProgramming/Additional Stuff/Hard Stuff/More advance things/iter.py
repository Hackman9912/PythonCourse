# Python iterators

# mylist = [1, 2, 3, 4]
# for item in mylist:
#     print(item)

# def traverse(iterable):
#     it = iter(iterable)
#     while True:
#         try:
#             item = next(it)
#             print(item)
#         except: StopIteration:
#             break
    

l1 = [1, 2, 3]
it = iter(l1)
# print next iteration in list
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# or you can use this
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

# some objects are not itreable and will error
iter(100)