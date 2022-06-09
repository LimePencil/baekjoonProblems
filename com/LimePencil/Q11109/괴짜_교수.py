import sys

input = sys.stdin.readline
for _ in range(int(input())):
    d,n,s,p=list(map(int,input().split()))
    normal=s*n
    parallel=n*p+d
    print("does not matter" if normal==parallel else ("parallelize" if normal>parallel else "do not parallelize"))