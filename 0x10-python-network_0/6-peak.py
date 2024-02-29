#!/usr/bin/python3
"""find peak"""


def find_peak(list_of_integers):
    """find peak"""
    # Base case: if the list is empty
    if not list_of_integers:
        return None
    
    # Function to find peak recursively
    def find_peak_recursive(start, end):
        if start == end:
            return list_of_integers[start]
        
        mid = (start + end) // 2
        # Check if the middle element is greater than or equal to its neighbors
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        # If the left neighbor is greater, then there must be a peak in the left half
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return find_peak_recursive(start, mid - 1)
        # If the right neighbor is greater, then there must be a peak in the right half
        else:
            return find_peak_recursive(mid + 1, end)
    
    # Initial call to the recursive function
    return find_peak_recursive(0, len(list_of_integers) - 1)
