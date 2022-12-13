import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    s,*arr = list(map(int,input().split()))
    can=True
    for i in range(1,s):
        if arr[i]<2*arr[i-1]:
            can=False
            break

    print("Denominations:",*arr)
    print("Good coin denominations!" if can else "Bad coin denominations!")
    print()