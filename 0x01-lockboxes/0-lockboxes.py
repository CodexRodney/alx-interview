#!/usr/bin/python3
"""
Defines a function canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened else
    return true
    A key with the same number as a box can be opened
    """
    pos = 0
    keys = set()
    len_box = len(boxes) - 1
    if boxes[0] == []:
        return False
    keys.update(boxes[0])
    while pos < len_box:
        new_keys = set()
        for z in keys:
            if z > len_box:
                continue
            new_keys.update(boxes[z])
        keys.update(new_keys)
        pos += 1
        if pos not in keys:
            return False
    return True
