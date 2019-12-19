# This class will represent a singly linked node

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
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    # Add things to the end of our linked list
    def append(self, data):
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
        # Anything in our linked list?
        newNode.next = self.head
        self.head = newNode
    # Inserting within the linked list
    def insert_node(self, index, data):
        # If the linked list is empty or index is less than 0
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
    # Remove a node
    def delete_node(self, index):
        # is this the only node?
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
            return removedItem
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
            return removedItem

    '''
    4. Modify delete to find the data you want to delete rather than an index.
    Modify delete to take in either an index or data.
    '''

    def flex_delete(self):
        selection = 0
        while selection != 1 and selection != 2:
            selection = int(input("If you want to delete by index press 1 or 2 to delete by value: "))
        if selection == 1:
            index = int(input("Enter the index of the data you want to delete: "))
            self.delete_node(index)
        elif selection == 2:
            value = input("Enter the value or data you want to delete exactly: ")
            index = 0
            probe = self.head
            while probe != None:
                if str(probe.data) == str(value):
                    self.delete_node(index)
                    index -= 1
                index += 1
                probe = probe.next
    
    def get_data(self, index):
        probe = self.head
        while index > 1:
            if probe.next == None:
                print("That index is out of range for index 1: ")
                exit()
            else:
                probe = probe.next
                index -= 1
        return probe.data

    def put_data(self, data, index):
        probe = self.head
        while index > 1:
            if probe.next == None:
                print("That index is out of range for index 1: ")
                exit()
            else:
                probe = probe.next
                index -= 1
        probe.data = data


    def swap_node(self, index1, index2):
        if self.head is None:
            print("There is no data in the list:")
        else:
            variable1 = self.get_data(index1)
            variable2 = self.get_data(index2)
            self.put_data(variable1, index2)
            self.put_data(variable2, index1)
    
    def get_len(self):
        count = 0
        probe = self.head
        while probe.next != None:
            count += 1
            probe = probe.next
        return count

    # 3. Implement a reverse method to singly and doubly.
    def reverse(self):
        if self.head is None:
            print("There is no data in the list:")
        else:
            count = self.get_len()+1
            index = 1
            while count > index:
                variable1 = self.get_data(index)
                variable2 = self.get_data(count)
                self.put_data(variable1, count)
                self.put_data(variable2, index)
                count -= 1
                index += 1

    def count_occurance(self):
        counter = 0
        item = input("Enter the item you want to count the amount of in the list: ")
        probe = self.head
        while probe != None:
            if str(probe.data) == str(item):
                counter += 1
            probe = probe.next
        print(f'There are {counter} of {item}.')





linked_list = LinkedList()
linked_list.append("4")
linked_list.append("5")
linked_list.prepend("2")
linked_list.prepend("1")
linked_list.prepend("1")
# linked_list.insert_node(0, "This sucks")
linked_list.insert_node(2, "3")
linked_list.insert_node(24, "6")
# linked_list.swap_node(2, 6)
linked_list.reverse()
linked_list.flex_delete()
linked_list.print_linked_list()

'''
Circular Linked List - Special case of singly linked list
                    Insertion and removal of the first node are special cases of the insert ith
                    and remove ith operations on a singly linked list. These are special because
                    the head pointer must be reset. You can use circular linked lists with a dummy
                    header node. Contains a link from the last node back to the first node in the 
                    structure.
'''

'''

    1. Finish out your doubly and circular linked list to add more functionality
        - prepend
        - insert
        - delete
        - print
'''

class CircularLinked:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            newNode = Node(data)
            probe = self.head
            while probe.next != self.head:
                probe = probe.next
            probe.next = newNode
            newNode.next = self.head

    def prepend(self, data):
        # instantiate a new Node object
        probe = self.head
        newNode = Node(data, self.head)
        # Anything in our linked list?
        while probe.next != self.head:
            probe = probe.next
        probe.next = newNode
        self.head = newNode

    # Inserting within the linked list
    def insert_node(self, index, data):
        # If the linked list is empty or index is less than 0
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
            self.head.next = self.head
        # Find our position to insert
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            # Insert new node after node at position index -1 or last position
            probe.next = Node(data, probe.next)

    # Remove a node
    def delete_node(self, index):
        # is this the only node?
        if index <= 0 or self.head.next is self.head:
            removedItem = self.head.data
            self.head = None
            return removedItem
        else:
            probe = self.head
            while index > 1 and probe.next.next != self.head:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
            return removedItem







# # Just an empty link
# node1 = None

# # A node containing data and an empty link
# node2 = Node("A", None)
# node3 = Node("B", node2)

# # print(node3.data)