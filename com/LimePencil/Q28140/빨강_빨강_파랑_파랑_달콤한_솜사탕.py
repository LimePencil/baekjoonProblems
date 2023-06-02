import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
n,q = list(map(int,input().split()))
s=input()
red = []
blue = []
for i in range(n):
    if s[i] == "R":
        red.append(i)
    elif s[i]== "B":
        blue.append(i)
for _ in range(q):
    l,r=map(int,input().split())
    left_red=bisect.bisect_left(red,l)
    right_red=bisect.bisect_right(red,r)
    if right_red-left_red<2:
        print(-1)
    else:
        left_blue=bisect.bisect_left(blue,red[left_red+1])
        right_blue=bisect.bisect_right(blue,r)
        if right_blue-left_blue<2:
            print(-1)
        else:
            print(red[left_red],red[left_red+1],blue[left_blue],blue[left_blue+1])