import sys
import random
import os
3yh
fileIn = sys.argv[1]
fileOut = sys.argv[2]

file_in = (fileIn, 'r')
file_out = (fileOut, 'w')

def isConnected(arr):
    conns = [False for i in range (0,nodes)]
    conns[0] = True
    for i in arr:
        for j in arr:
            if conns[j[0]]:
                conns[j[1]] = True
            if all(conn for conn in conns):
                return True
    return False
