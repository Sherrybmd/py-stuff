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

    section = s[-2:]  # grab PM/AM
    mytime = s[:-2]     # grab 00:00:00 time

    hour = int(mytime[:2])


    if section == 'PM':

        if hour < 12:
            hour += 12

        hour = str(hour)
        mytime = mytime.replace(mytime[:2], hour)


    elif section == 'AM':

        if hour < 12:
            if hour < 10:        # put 0 for one digit hours

                hour = str(hour)
                hour = '0' + hour


        elif hour == 12:

            hour = str(hour)
            hour = '00'

        hour = str(hour)
        mytime = mytime.replace(mytime[:2], hour)

    return mytime


s = '12:01:01AM'

print(timeConversion(s))
