import sys
import math

d,w,h = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
mul = d/math.sqrt(w**2+h**2)
print(str(math.floor(mul*w))+ " "+ str(math.floor(mul*h)))