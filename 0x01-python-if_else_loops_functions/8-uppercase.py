#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{}".format(ord(i) - 32), end='')
    print()
