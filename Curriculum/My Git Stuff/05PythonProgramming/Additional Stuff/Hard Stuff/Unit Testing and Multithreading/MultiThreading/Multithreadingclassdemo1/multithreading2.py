# For editing further without losing multithreading og file

'''
RUnning things concurrently is known as multithreading
Running things in parallel is known as multiprocessing

I/O bound tasks - Waiting for input and output to be completed
                    reading and writing from file system, network
                    operations.
                    These all benefit more from threading
                    You get the illusion of running code at the same time,
                        however other code starts running while other code is waiting

CPU bound tasks - Good for number crunching
                    Using CPU
                    Data Crunching
                    These benefit more from multiprocessing and running in parallel
                    Using multiprocessing might be slower if you have overhead from creating
                    and destroying files.



                    RUN 10 THREADS IN THIS VERSION


        We can also pass in an argument for seconds
'''
import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second....')
    time.sleep(seconds)
    print('Done Sleeping....')
# initialize list of threads
threads = []

# Setup loop to start 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something, args = [1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finished = time.perf_counter()


print(f'Our program finished in {finished - start:.6f} seconds.')