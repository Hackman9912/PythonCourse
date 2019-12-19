'''
******************************** Collection Types ******************************************
    Collections

        A group of 0 or more items that can be treated as a conceptual unit. Things like strings, lists, tuples, dictionaries.

        Other types of collections: stacks, queues, priority queues, binary search trees, heaps, graphs, and bags. 


    Images showing the below examples are found in: 
    https://github.com/Hackman9912/06-Intro-to-Algorithms/tree/master/Algorithms



    Linear Collection - like people in a line, they are ordered by position

        each item except the first has a unique predecessor(position in line)

        D1 ---- D2 ------ D3 ------ D4 ------D5

        Examples are grocery lists, stacks of dinner plates, and a line at the atm


    Hierarchical Collection - ordered in a structure resembling an upside down tree.

        Each data item except the one at the top has just one predecessor called its parent, but potentially has many successors called children

        Examples include a file directory system, a companies organizational tree, and a books table of contents


    Graph Collection - Also called graph, each item can have many predecessors and many successors. These are also called neighbors.

        Examples include: airline routes between cities, electrical wiring diagrams, and the world wide web. 

    Unordered Collections - these are not in any particular order, and its not possible to meaningfully speak of an items predecessor or successor. 

        Examples include a bag of marbles


******************************** Operation Types *******************************************

    Operations can be applied to any Collection to take the listed action

    Determine the size - Use Python's len function to obtain the number of items currently in the collection

    Test for item membership - Use Python's in operator to search for a given target item in the colleciton. Returns True if the item is found
        and False otherwise

    Traverse the collection - Use python's for loop to visit each item in the collection. The order which items are visited depends on the type of collection.

    Obtain a string representation - Use Pythons str function to obtain the string representation of the collection

    Test for equality - Use Pythons == operator to determine wheter two collections are equal. Two collecitons are equal if they are of the same type and 
        Contain the same items. The order in which pairs of items are compared depends on the type of collection.

    Concatentate two collections - Use Python's + operator to obtain a new colleciton of the same type as the operands, and containing the items of the two. 

    Convert to another type of collection - Create a new collection with the same items as a source collection.

    Insert an item - Add the item to the collection, possibly at a given position

    Remove an item - Remove the item from the colection, possibly at a given position

    Replace an item - Combine removal and insertion into one operation

    Access or retrieve an item - Obtain an item, possibly at a given position
'''