# Doubly Linked Lists - Very similar to singly linked, however these have prev pointer
#                       and a tail node
#                       Move left, to previous node, from a given node
#                       Move immediately to the last node

'''

    1. Finish out your doubly and circular linked list to add more functionality
        - prepend
        - insert
        - delete
        - print
'''
class DoubleNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_linked_list(self):
        probe = self.head
        print(f"Here is the tail item first..?: {self.tail.data}")
        print('Now here is your data')
        while probe != None:
            print(probe.data)
            probe = probe.next

    # Two cases to consider
    def append(self, data):
        newNode = DoubleNode(data)
        # empty linked list?
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.tail = self.head
        # We have items in our list
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next

    def prepend(self, data):
        if self.head is None:
            self.append(data)
        else:
            newNode = DoubleNode(data, self.head)
            self.head.prev = newNode
            self.head = newNode

    def insert_node(self, index, data):
        if self.head is None or index <= 0:
            self.append(data)
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            newNode = DoubleNode(data, probe.next, probe.prev)
            if probe.next.next != None:
                probe.next.prev = newNode
            probe.next.prev = newNode
            probe.next = newNode
            newNode.prev = probe
            
    def delete_node(self, index):
        # is this the only node?
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return removedItem
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            if self.tail.data == removedItem:
                self.tail = probe
            if probe.next.next != None:
                probe.next.next.prev = probe
            else:
                probe.next.prev = probe.prev
            probe.next = probe.next.next
            while probe.next != None:
                probe = probe.next
            self.tail = probe
            return removedItem

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
                    print(f'DELETED {self.delete_node(index)}')
                    index -= 1
                index += 1
                probe = probe.next

    def get_data(self, index):
        probe = self.head
        while index > 0:
            if probe.next == None:
                print("That index is out of range: ")
                exit()
            else:
                probe = probe.next
                index -= 1
        return probe.data

    def put_data(self, data, index):
        probe = self.head
        while index > 0:
            if probe.next == None:
                print("That index is out of range: ")
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
    '''
    3. Implement a reverse method to singly and doubly.
    '''
    def reverse(self):
        if self.head is None:
            print("There is no data in the list:")
        else:
            count = self.get_len()
            index = 0
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

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("2")
doubly_linked_list.append([1, 2, "Howdy"])
doubly_linked_list.prepend("1")
doubly_linked_list.insert_node(2, "3")
doubly_linked_list.delete_node(4)
doubly_linked_list.append([4])
doubly_linked_list.swap_node(0,1)
doubly_linked_list.reverse()
doubly_linked_list.flex_delete()
doubly_linked_list.append("TEST")
doubly_linked_list.count_occurance()
doubly_linked_list.print_linked_list()
