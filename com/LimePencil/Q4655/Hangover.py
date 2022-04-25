import sys

input = sys.stdin.readline
while True:
    n = float(input())
    if n==0.00:
        break
    ans=2
    s=0
    while True:
        s+=1/ans
        ans+=1
        if s>=n:
            break
    print("{} card(s)".format(ans-2))