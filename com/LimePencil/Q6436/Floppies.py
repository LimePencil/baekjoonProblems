from math import ceil
import sys

input = sys.stdin.readline
cnt=1
while True:
    n=int(input())

    if n==0:
        break
    n=n/2
    n*=1.5
    n/=1860000
    print(f"File #{cnt}")
    print(f"John needs {ceil(n)} floppies.")
    print()
    cnt+=1