#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            c = chr(ord(c) - (ord("a") - ord("A")))
        result += c
        print("{:s}".format(result))
