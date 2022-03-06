import sys
import math

input = sys.stdin.readline
arr = list(map(int,input().split(" ")))
print(math.ceil(arr[0]/arr[2])*math.ceil(arr[1]/arr[2]))