#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary.keys())
    return {i: a_dictionary[i] * 2 for i in keys}
