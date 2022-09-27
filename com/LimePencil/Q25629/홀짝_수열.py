import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
odd=0
even=0
for a in arr:
    if a%2==0:
        even+=1
    else:
        odd+=1
print(1 if (odd-1==even and n%2==1) or (odd==even and n%2==0) else 0)