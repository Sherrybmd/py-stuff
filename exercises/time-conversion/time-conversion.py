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


    # s[0:2]

    section = s[-2:]  # grab PM/AM
    mytime = s[:-2]     # grab 00:00:00 time

    hour = int(mytime[:2])

    if section == 'PM':
        print("true")

        if hour < 12:
            hour += 12
        hour = str(hour)

        mytime = mytime.replace(mytime[:2], hour)

    elif section == 'AM':

        print("false")
        if hour < 12:

            if hour < 10:

                hour = str(hour)
                hour = '0' + hour


        elif hour == 12:

            hour = str(hour)
            hour = '00'

        hour = str(hour)
        print(hour)
        mytime = mytime.replace(mytime[:2], hour)



    return mytime


s = '12:01:01AM'

print(timeConversion(s))
