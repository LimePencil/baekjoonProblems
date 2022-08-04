import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
friend = [0]*n
for _ in range(m):
    a,b=list(map(int,input().split()))
    friend[a-1]+=1
    friend[b-1]+=1
print(*friend,sep="\n")