#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char is not 'c' and char is not 'C':
            new_string += char
    return new_string
