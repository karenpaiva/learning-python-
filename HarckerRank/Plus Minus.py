import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
        positivo=0
        negativo=0
        neutro=0
        tamanho=len(arr)
        for x in arr:
            if x==0:
                neutro+=1
            elif x<0:
                negativo+=1
            else:
                positivo+=1
        print(' {0:.6f}'.format(positivo/tamanho),'\n','{0:.6f}'.format(negativo/tamanho),'\n','{0:.6f}'.format(neutro/tamanho))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
