import sys

input = sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    fare=[int(input()) for _ in range(n-1)]
    stations=[input().rstrip() for _ in range(n)]
    print(f"Data Set {i+1}:")
    print(fare[abs(stations.index(input().rstrip())-stations.index(input().rstrip()))-1])
    print()