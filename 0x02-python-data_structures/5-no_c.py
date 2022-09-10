#!/usr/bin/python3
def no_c(my_string):
    new_string = [i for i in my_string if i not in ['c', 'C']]
    new_string = ''.join(new_string)
    return new_string
