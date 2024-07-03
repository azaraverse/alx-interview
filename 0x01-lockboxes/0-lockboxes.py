#!/usr/bin/python3
"""
Lockboxes Challenge

Using Adjacency List Representation to represent my lockbox.
Example list:       [[1, 2], [0, 2], [0, 1, 3], [2]]
Vertices/Indexes:   [0], [1], [2], [3]

Using the lockboxes logic, the vertices represent the boxes, and the
lists represent the keys contained in each box.

More simplified representation for my understanding;
0[1, 2], 1[0, 2], 2[0, 1, 3], 3[2]

Challenge:
The challenge is to check if a vertex/box can unlock or contains the keys
to the vertices/boxes adjacent to it.

Vertex/Box [0] contains the keys to vertices/boxes [1] and [2]
Vertex/Box [1] contains the keys to vertices/boxes [0] and [2]
Vertex/Box [2] contains the keys to vertices/boxes [0], [1] and [3]
Vertex/Box [3] contains the keys to vertex/box [2]
"""


def canUnlockAll(boxes=[[]]):
    """
    n number of boxes given. Each box is numbered sequentially from
    0 to n - 1 and each box may contain keys to the other boxes.

    A key with the same number as a box opens that box. If there is
    a box that contains a key with same number as the key that has
    its own number, then latter can be opened. Otherwise, can't be
    opened.

    Our first box must be always unlocked.

    boxes (list of lists): List of lists.

    Returns (boolean): True if all boxes can be unlocked. Otherwise,
    False
    """
    # create a list that will track all opened boxes. set opened to false
    # initially and set it to true if all tracked boxes are opened
    # multiply the boolean by the number of boxes available
    opened = [False] * len(boxes)
    # check the correct output of opened
    # print('Check all boxes are initialised to False:')
    # print(opened)

    # set the first box in opened to true since it has to be always opened
    opened[0] = True
    # check if first box is set to true
    # print('Check first box is initialised to True:')
    # print(opened)

    # initialise a list of keys to keep track of keys we have collected,
    # beginning with the key to box 0
    keys = [0]

    # Perform BSF - Breadth-First Search
    # while we have keys in our list
    while keys:
        # Take the first key from the list and hold it in a variable
        current_key = keys.pop(0)
        # check if the first key has been taken
        # print('Checking if current key has been taken:')
        # print(current_key)
        # for every key found in the current box
        for key in boxes[current_key]:
            # print('Each key in the box being iterated over:')
            # print(key)
            # check if key is within valid range of box indices
            if key >= 0 and key < len(boxes):
                # if the box corresponding to the key has not been opened yet
                if not opened[key]:
                    # mark box as opened
                    opened[key] = True
                    # print('A box has just been opened:')
                    # print(opened)
                    # add the key to list of keys to use later
                    keys.append(key)
                    # print('List of keys that has been used tracker:')
                    # print(keys)
    # print('All boxes:')
    # print(opened)

    # now check if all boxes are opened
    # if all values in opened are true, otherwise, return false
    if all(opened):
        return True
    return False
