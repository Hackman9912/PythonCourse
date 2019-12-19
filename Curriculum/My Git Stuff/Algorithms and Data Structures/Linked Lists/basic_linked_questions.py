'''
1. Using box and pointer notation, draw a picture of the nodes created by the 
first loop in the tester program. 

       _        _ __  ___        _ __  ___        _ __  ___        _ __  ___        _ __  ___  ___
 head |_|----->|_D1_||_5_|----->|_D2_||_4_|----->|_D3_||_3_|----->|_D4_||_2_|----->|_D5_||_1_||_/|

2. What happens when a programmer attempts to access a node’s data fields when 
the node variable refers to None? How do you guard against it?
You get an attribute error
You assign a link

3. Write a code segment that transfers items from a full array to a singly linked 
structure. The operation should preserve the ordering of the items.
'''
# import node
from node import Node
# set head to none
head = None
# make the list
list1 = [1,2,3,4,5]
# get the length of the list
length = len(list1) - 1
# iterate the length of the list
for count in range(len(list1)):
    # send the end of the list to Node as head using length
    head = Node(list1[length], head)
    # take 1 from legth
    length -= 1

# Print the contents of the structure
while head != None:
    print(head.data)
    head = head.next
    