# Zip function
# This is a good way to take two different sequences of data and pair them together

# Set up two lists
prices = [72.51, 9.27, 153.74, 53.00]
names = ['CAT', 'GE', 'MSFT', 'AA', 'IBM']

# use for loop and zip() to pair the lists together

for name, price in zip(names, prices):
    print(name, '=', price)