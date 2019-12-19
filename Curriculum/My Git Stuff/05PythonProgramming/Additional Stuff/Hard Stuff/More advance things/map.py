# The map() function
# Takes in at least 2 args. Can apply a function to every item in a list/iterable quickly

def square(x):
    return x*x

numbers = [1, 2, 3, 4, 5]
squarelist = map(square, numbers)
print(next(squarelist))
print(next(squarelist))
print(next(squarelist))
print(next(squarelist))
print(next(squarelist))


sqrlist2 = map(lambda x : x*x, numbers)
print(next(sqrlist2))
print(next(sqrlist2))
print(next(sqrlist2))
print(next(sqrlist2))
print(next(sqrlist2))

tens = [10, 20, 30, 40, 50]
indx = [1, 2, 3, 4, 5]
powers = list(map(pow, tens, indx[:3]))
print(powers)
