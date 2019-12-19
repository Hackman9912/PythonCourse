# Generator
# a special function that does not return a single value but rather an iterator object with a sequence of values

def myGenerator():
    print('First item')
    # yield is how you return data in a generator. A return will break it. 
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = myGenerator()

print(next(gen))
print(next(gen))
print(next(gen))
