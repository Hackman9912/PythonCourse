# This prints the running times ofr problem sizes that double using a single loop

import time

problemSize = 1000

for count in range(5):
    start = time.time()
    # The start of the algorithm
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1
    # The end of the algorithm
    elapsed = time.time() - start
    print(f'{problemSize} - {elapsed}')
    problemSize *= 2