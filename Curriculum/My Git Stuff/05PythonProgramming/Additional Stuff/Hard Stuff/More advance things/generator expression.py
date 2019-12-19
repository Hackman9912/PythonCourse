# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

my_gen2 = (n*n for n in nums)
for i in my_gen2:
    print(i)