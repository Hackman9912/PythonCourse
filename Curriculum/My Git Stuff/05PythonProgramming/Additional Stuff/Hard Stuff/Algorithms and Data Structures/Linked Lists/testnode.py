# This file will test the Node class

from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next
    
'''
- One pointer, head, generates the linked structure. This pointer is manipulated
    in such a way that the most recently inserted item is always at the beginning
    of the structure.
- When the data is displayed it appears in the reverse order of its insertion
- Also, when the data is displayed, the head pointer, is reset to the next node, until
    the head pointer becomes None. Thus, at the end of this process, the nodes are effectively 
    deleted from the linked structure. They are no longer available to the program and are
    recycled duritng the next garbage colleciton.
'''