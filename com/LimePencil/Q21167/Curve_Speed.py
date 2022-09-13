import sys

input = sys.stdin.readline
while True:
    try:
        r,s=list(map(float,input().split()))
        print(round(((r*(s+0.16))/0.067)**0.5))
    except:
        break