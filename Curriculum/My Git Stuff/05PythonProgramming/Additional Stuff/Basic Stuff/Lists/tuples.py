# tuples are like an immutable list

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)

# printing items in a tuple

names = ('Holly', 'Warren', 'Ashley')

for n in names:
    print(n)

for i in range(len(names)):
    print (names[i])


# Convert between a list and a tuple

listA = [2, 4, 5, 1, 6]

type(listA)

tuple(listA)

type(listA)

tupA = tuple(listA)

type(tupA)