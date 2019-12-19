# For editing further without losing multithreading og file

'''
Prove that these are actually coming in as they are completed
    Lets pass in a range of seconds

Start 5 second thread first
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

    # map will apply the function do_something to every item in the seconds_list
    # insteatd of running the results as they complete, map returns in the order
    # that they were started
    results =  executor.map(do_something, seconds_list)

    for result in results:
        print(result)

finished = time.perf_counter()


print(f'Our program finished in {finished - start:.6f} seconds.')