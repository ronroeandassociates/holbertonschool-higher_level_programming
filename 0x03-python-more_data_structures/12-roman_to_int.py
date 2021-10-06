#!/usr/bin/python3
def roman_to_int(roman_string):
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    ival = 0
    rome = roman_string
    if type(roman_string) != str or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and letters[rome[i]] > letters[rome[i-1]]:
            iVal += letters[rome[i]] - \
                    2 * letters[rome[i-1]]
        else:
            ival += letters[rome[i]]
    return ival            
