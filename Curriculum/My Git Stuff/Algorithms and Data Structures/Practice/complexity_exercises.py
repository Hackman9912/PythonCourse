"""
1. Assume that each of the following expressions indicates the number of 
operations performed by an algorithm for a problem size of n. Point out 
the dominant term of each algorithm and use big-O notation to classify it. 

    a. 2^n - 4n^2 + 5n
        O(2^n)
    b. 3n^2 + 6
        O(n^2)
    c. n^3 + n^2 - n
        O(n^3)
2. For problem size n, algorithms A and B perform n^2 and (1/2)n^2 + (1/2)n 
instructions, respectively. 
Which algorithm does more work? 
B does more work until the numbers get larger then A will be doing more work

Are there particular problem sizes for which one algorithm performs significantly better than the 
other? 
Yes

Are there particular problem sizes for which both algorithms perform 
approximately the same amount of work?
Yes


3. At what point does an n^4 algorithm begin to perform better than a 2^n algorithm?

"""

n = 0

while (2 ** n) > (n ** 4):
    print(f'a is {(2 ** n)}, b is {(n ** 4)}, for n {n}')
    n += 1

print(f'Final {n ** 4}')
