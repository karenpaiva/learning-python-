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
    horas=int(s[0:2])
    if s[-2:]=='AM' and horas==12:
        return('00'+s[2:8])
    elif  s[-2:]=='PM' and horas==12:
        return(str(horas)+s[2:8])
    elif s[-2:]=='PM':
        horas+=12
        return(str(horas)+s[2:8])
    else:
       return(s[:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
