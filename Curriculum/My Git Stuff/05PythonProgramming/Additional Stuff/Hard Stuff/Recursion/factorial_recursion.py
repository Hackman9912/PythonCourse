# function definition
def recursive_factoriable(n):
    # Base case
    if n == 0:
        return 1
    # recursive case
    else:
        return n * recursive_factoriable(n-1)

print(recursive_factoriable(4))