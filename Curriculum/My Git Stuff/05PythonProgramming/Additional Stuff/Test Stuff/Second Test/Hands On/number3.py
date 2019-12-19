"""

#******************************************************

3. Singly Linked Lists
    Implement an insert_before() and insert_after() function for singly linked lists.
    insert_before takes in an index as an argument and inserts the node before the given
        index. (Its possible we already did this in class...)
    insert_after takes in an index as an argument and inserts the node after the given
        index.

"""
# define the class of node
class Node:
    def __init__(self, data, next = None):
        # Instantiates a Node with a default next of None
        self.data = data
        self.next = next
# This Linked class will instantiate Node objects and we'll add methods 
# to this class to add functionality
class LinkedList:
    def __init__(self):
        self.head = None

    # printing our linked list
    def print_linked_list(self):
        # set probe to self.head
        probe = self.head
        # while the probe does not equal None
        while probe != None:
            # print the data and then move to the next line
            print(probe.data)
            probe = probe.next

    # Add things to the end of our linked list
    def append(self, data):
        # build a new nodw
        newNode = Node(data)
        # Is there something in our linked list yet?
        if self.head is None:
            self.head = newNode
        # There are node(s) in our linked list
        else:
            probe = self.head
            # Is probe at the end of the linked list?
            while probe.next != None:
                probe = probe.next
            probe.next = newNode
    # Add things to the beginning of our linked list
    def prepend(self, data):
        # instantiate a new Node object
        newNode = Node(data)
        # Anything in our linked list? Go ahead and add your node to the beginning
        newNode.next = self.head
        self.head = newNode
    # Inserting within the linked list THIS TAKES THE PLACE OF THE CURRENT VALUE IN THAT INDEX THUS PLACING THIS BEFORE THAT VALUE
    def insert_before(self, index, data):
        # If the linked list is empty or index is less than 0 then just set head to the thing
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        # Find our position to insert
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # Insert new node after node at position index -1 or last position
            probe.next = Node(data, probe.next)
    # Inserting within the linked list THIS TAKES THE PLACE AFTER THE CURRENT VALUE IN THAT INDEX THUS PLACING THIS AFTER THAT VALUE
    def insert_after(self, index, data):
        # If the linked list is empty or index is less than 0
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        # Find our position to insert
        else:
            probe = self.head
            while index > 0 and probe.next != None:
                probe = probe.next
                index -= 1
            # Insert new node after node at position index +1 or next position
            probe.next = Node(data, probe.next)


linked_list = LinkedList()
linked_list.append("3")
linked_list.append("4")
linked_list.prepend("2")
linked_list.prepend("1")
linked_list.prepend("0")
linked_list.insert_before(4, "test1")
linked_list.insert_after(5, "test2")
linked_list.print_linked_list()