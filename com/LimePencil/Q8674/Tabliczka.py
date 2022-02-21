import sys

input = sys.stdin.readline
w,h = list(map(int,input().split(" ")))

if h%2 ==0 or w%2==0:
    print("0")
elif h>=w:
    print(w)
else:
    print(h)