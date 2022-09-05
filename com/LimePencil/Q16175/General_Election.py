import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    arr=[list(map(int,input().split())) for _ in range(m)]
    s=[sum([arr[j][i] for j in range(m)]) for i in range(n)]
    print(s.index(max(s))+1)