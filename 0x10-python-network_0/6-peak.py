#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    finding the peak
    """
    max_number = None
    for num in list_of_integers:
        if max_number is None or max_number < num:
            max_number = num
    return max_number
