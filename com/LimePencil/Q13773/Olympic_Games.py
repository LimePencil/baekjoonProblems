import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n==0:
        break
    if n%4==0 and n>=1896:
        if 1914<=n<=1918 or 1939<=n<=1945:
            print(n,"Games cancelled")
        elif n>=2024:
            print(n,"No city yet chosen")
        else:
            print(n,"Summer Olympics")
    else:
        print(n,"No summer games")