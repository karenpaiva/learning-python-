import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    nova_lista=[]
    dicts = {}

    for palavra in a:
        nova_lista.append(a.count(palavra))
    for i in range(n):
        dicts[a[i]] = nova_lista[i]
    for key, value in dicts.items():
         if value==1:
            return(key)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
