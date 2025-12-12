#!/usr/bin/python3
"""Module to determine if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    
    Args:
        boxes: list of lists containing keys
    
    Returns:
        True if all boxes can be opened, False otherwise
    """
    n = len(boxes)
    opened = {0}
    keys = set(boxes[0])
    
    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in opened:
            opened.add(new_key)
            keys.update(boxes[new_key])
    
    return len(opened) == n