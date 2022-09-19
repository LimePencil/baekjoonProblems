from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

def BFS():
    q=deque()
    q.append((0,a))
    while q:
        dist,node=q.popleft()
        if node==b:
            return dist
        for i in range(arr[node],n+1,arr[node]):
            if 0<node+i<n+1:
                q.append((dist+1,node+i))
            if 0<node-i<n+1:
                q.append((dist+1,node-i))
    return -1


n = int(input())
arr = [0]+list(map(int,input().split()))
a,b=list(map(int,input().split()))
print(BFS())