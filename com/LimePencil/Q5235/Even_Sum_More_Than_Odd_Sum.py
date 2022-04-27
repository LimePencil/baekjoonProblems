import sys

input = sys.stdin.readline
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    odd=0
    even=0
    for n in arr[1:]:
        if n%2==0:
            even+=n
        else:
            odd+=n
    print("TIE" if odd==even else "EVEN" if even>odd else "ODD")