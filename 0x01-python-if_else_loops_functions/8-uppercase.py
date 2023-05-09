#!/usr/bin/python3
def uppercase(s):
    for c in s:
        ascii_code = ord(c)
        if ascii_code >= 97 and ascii_code <= 122:
            ascii_code -= 32
        print("{}".format(chr(ascii_code)), end="")
        print("")
