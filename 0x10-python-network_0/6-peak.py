#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) >= 2:
        return max(list_of_integers)
