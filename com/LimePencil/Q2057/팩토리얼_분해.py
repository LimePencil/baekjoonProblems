from math import factorial
import sys

input = sys.stdin.readline
arr = [factorial(i) for i in range(21)]
n = int(input())
if n==0:
    print("NO")
    exit()
for a in range(20,-1,-1):
    if n>=arr[a]:
        n-=arr[a]
if n==0:
    print("YES")
else:
    print("NO")