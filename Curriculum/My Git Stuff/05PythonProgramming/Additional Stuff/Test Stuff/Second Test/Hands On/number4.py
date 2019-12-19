"""

4. Doubly Linked Lists
    Implement a reverse function by using the doubly linked list below. Do this 
    without using the tail node. 

#******************************************************
    class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    class DoublyLinkedList:
        def __init__(self):
            self.head = None

        # Two cases, empty list and list with items
        def append(self, data):
            newNode = Node(data)
            if self.head is None:
                newNode.prev = None
                self.head = newNode            
            else:
                probe = self.head
                while probe.next != None:
                    probe = probe.next
                newNode.prev = probe
                probe.next = newNode

        def print_list(self):
            probe = self.head
            while probe != None:
                print(probe.data)
                probe = probe.next

        def insert_node(self, index, data):
            probe = self.head
            while probe != None:
                if probe.next is None and probe.data == index:
                    self.prepend(data)
                elif probe.next == index:
                    newNode = Node(data)
                    prev = probe.prev
                    prev.next = newNode
                    newNode.next = probe
                    newNode.prev = prev
                probe = probe.next

        def reverse(self):
            # implement this function

    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append("A")
    doubly_linked_list.append("b")
    doubly_linked_list.append([7,245,8,68,"hello"])
    doubly_linked_list.insert_node(1, "one")
    doubly_linked_list.print_list()
    doubly_linked_list.reverse()
    doubly_linked_list.print_list()
#******************************************************

"""
# Define our class of Node
class Node:
    # initialize the class
    def __init__(self, data, next = None, prev = None):
        # establish the variables/the selfs
        self.data = data
        self.next = next
        self.prev = prev
# Define our class of DoublyLinkedList
class DoublyLinkedList:
    # initialize the class
    def __init__(self):
        self.head = None

    # Two cases, empty list and list with items
    def append(self, data):
        # build the new item
        newNode = Node(data)
        # if the list is empty then add the thing and make it a list
        if self.head is None:
            newNode.prev = None
            self.head = newNode            
        # if not then go to the end of the list and add it there
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            newNode.prev = probe
            probe.next = newNode
    # print the items in the list
    def print_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
    # add things at the beginning of the list
    def prepend(self, data):
        # if the list is empty then call the append function
        if self.head is None:
            self.append(data)
        else:
        # if it is not empty then add the item in front of the current head
            newNode = Node(data, self.head)
            self.head.prev = newNode
            self.head = newNode
    # define the insert_node function that works
    def insert_node(self, index, data):
        # if the list is empty or the index is less than 0 then send to prepend
        if self.head is None or index <= 0:
            self.prepend(data)
        # if not then insert the list
        else:
            # set probe to self.head
            probe = self.head
            # while the index is a valid variable and probe.next is something then keep moving
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # build the new node
            newNode = Node(data, probe.next, probe.prev)
            # set the new node to take the position it is currently in
            if probe.next.next != None:
                probe.next.prev = newNode
            probe.next.prev = newNode
            probe.next = newNode
            newNode.prev = probe

    # Define the function to reverse the thing
    def reverse(self):
        # set the probe to be self.head
        probe = self.head
        # set prev1 and nextitem to be None
        prev1 = None
        nextitem = None
        # While probe is something
        while probe is not None:
            # set next item to be the thing after probe
            nextitem = probe.next
            # set the next pointer at probe to point at prev1
            probe.next = prev1
            # set prev1 to be probe
            prev1 = probe
            # set probe to be the next item
            probe = nextitem
        # now set head to be the prev1
        self.head = prev1
        # now set probe to be self.head again...
        probe = self.head
        # set probe.prev to be None
        probe.prev = None
        # While probe.next is something then set probe.next to point to probe
        while probe.next is not None:
            probe.next.prev = probe
            probe = probe.next



# Make our doubly list using append and insert and stuff
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("A")
doubly_linked_list.append("b")
doubly_linked_list.append("C")
doubly_linked_list.append([7,245,8,68,"hello"])
doubly_linked_list.insert_node(1, "one")
# print the OG list
doubly_linked_list.print_list()
# reverse it
doubly_linked_list.reverse()
# print the new list
doubly_linked_list.print_list()