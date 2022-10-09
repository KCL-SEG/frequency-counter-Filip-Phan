"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        str_item = str(item)
        if (str_item not in frequencies):
            frequencies[str_item] = 0
        frequencies[str_item] += 1
    return frequencies
