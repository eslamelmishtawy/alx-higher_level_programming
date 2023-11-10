#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = next(iter(a_dictionary.values()))
    name = next(iter(a_dictionary.keys()))
    for i, j in a_dictionary.items():
        if j > best_score:
            best_score = j
            name = i
    return name
