'''
Queues
    S linear colleciton that adds elements to one end and removes them from
        the other in a FIFO (first in first out) protocol
    Queues are implememnted in many ways, some based on arrays, and some based on linked structures

    rear - insertions are restricted to this end
    front - removals are restricted to this end

    Two fundamental operations, add and pop
        push - adds items to the rear
        pop - removes item from the front
        peek - see the item at the front of the queue

    There are priority queues that schedule their elements using a rating scheme
    as well as FIFO. If two elements have same rating then they are scheduled in 
    FIFO order. Elements are ranked from smallest to largest according to some attribute 
    like a number or char, generally smallest are removed first no matter 
    when they are added to the queue. (Dijkstra's shortest path algorithm)

'''

class Queue:
    def __init__(self):
        self.queue = []

    def push(self):
        item = input("What item would you like to push? ")
        self.queue.append(item)

    def pop(self):
        item = self.queue.pop(0)
        print("You popped", item)

    def peek(self):
        if self.queue:
            print(self.queue[0])

    def view_q(self):
        for i in range(len(self.queue)):
            print(f'Item {i}, is {self.queue[i]}')

q = Queue()

while True:
    print('-------------------')
    print('Queue Options')
    print('1. View Queue')
    print('2. See next in Queue')
    print('3. Push onto Queue')
    print('4. Pop out of Queue')
    print('5. To quit')
    print('-------------------')

    menu_choice = int(input('Choose your option: \n'))

    if menu_choice == 1:
        q.view_q()
    if menu_choice == 2:
        q.peek()
    if menu_choice == 3:
        q.push()
    if menu_choice == 4:
        q.pop()
    if menu_choice == 5:
        exit()