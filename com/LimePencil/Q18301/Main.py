import sys
import math

a,b,c = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
print(math.floor((a+1)*(b+1)/(c+1)-1))