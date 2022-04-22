import sys
import math

def DFS(s,e):
    stack = []
    visited = [False]*n
    stack.append((s,house[s]))
    visited[s] = True
    while stack:
        node,num= stack.pop()
        if node == e:
            return num
        for next_node in path[node]:
            if not visited[next_node]:
                visited[next_node] = True
                new_num = house[next_node]
                l = int(math.log10(new_num))+1
                stack.append((next_node,((num*10**l)%MOD+new_num%MOD)%MOD))    
MOD=1000000007
input = sys.stdin.readline
n,q = map(int,input().split())
house = list(map(int,input().split()))
path = [[]for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)

for _ in range(q):
    a,b = map(int,input().split())
    print(DFS(a-1,b-1))