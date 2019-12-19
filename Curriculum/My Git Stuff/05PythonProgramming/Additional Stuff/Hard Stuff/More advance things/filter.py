# Filter
# Filter takes in 2 args. A function and an iterable and only returns them if they are true

def isPrime(x):
    for n in range(2, x):
        if x % n == 0:
            return False
        
    return True

filterObject = filter(isPrime, range(10))
print('odd numbers between 1 and 10', list(filterObject))

# filter applied with lambda
filterObject2 = filter(lambda x : x % 2 != 0, range(10))
print(list(filterObject2))

#filter on a random list
randomlist = [1, 'a', 0, False, True, '0']
filterdlist = filter(None, randomlist)

print('The filtered elemetns are')
for element in filterdlist:
    print(element)