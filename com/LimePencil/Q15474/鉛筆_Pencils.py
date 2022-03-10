import sys
from math import ceil

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
print(min(ceil(arr[0]/arr[1])*arr[2],ceil(arr[0]/arr[3])*arr[4]))