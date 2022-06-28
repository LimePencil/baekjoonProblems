import sys

input = sys.stdin.readline
t,p = list(map(int,input().split()))
drained=100-p
normal=max(0,p-20)
eco=p-normal
rate=0
if drained>=80:
    rate=((drained-80)*2+80)/t
else:
    rate=drained/t
print(eco/(rate/2)+normal/rate)