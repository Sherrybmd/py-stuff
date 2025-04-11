import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):

    c = s.split(":")
    string = ""

    for item in c:
        for letter in item:
            if letter.isalpha():
                string += letter   # grab PM/AM
                letter.replace("")

    hours, minutes, seconds = c
    print(hours, minutes, seconds)
    '''
    AM -> 00:00:00 till 12:00:00
    PM -> 12:00:00 till 00:00:00
    '''

    return c


s = '12:01:01PM'

print(timeConversion(s))
