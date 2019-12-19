# For editing further without losing multithreading og file

'''
Prove that these are actually coming in as they are completed
    Lets pass in a range of seconds

Start 5 second thread first, but since we used as_completed() method it 
    prints the results in the order they are completed

    
'''
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second....')
    time.sleep(seconds)
    return f'Done Sleeping....{seconds}'

# using a context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds_list = [5, 4, 3, 2, 1]


    results = [executor.submit(do_something, sec) for sec in seconds_list]

    # to get the results we can use another function from future object that gives us an iterator
    # known as 'as_completed()'

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finished = time.perf_counter()


print(f'Our program finished in {finished - start:.6f} seconds.')