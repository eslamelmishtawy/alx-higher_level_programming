#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = next(iter(a_dictionary.values()))
    for i, j in a_dictionary.items():
        if j > best_score:
            best_score = j
    return best_score
