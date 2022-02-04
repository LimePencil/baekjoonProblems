import sys

a,b,c = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

print(round(0.229*0.324*a*2+0.297*0.42*2*b+0.21*0.297*c,6))

