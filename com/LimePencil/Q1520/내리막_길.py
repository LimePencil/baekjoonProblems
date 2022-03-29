# BFS with priority queue
import sys
import heapq

def BFS():
    queue = [(table[0][0],0,0)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        h,x,y = heapq.heappop(queue)
        for dx,dy in direction:
            nx=dx+x
            ny=dy+y
            if 0<=nx<n and 0<=ny<m and table[nx][ny]<table[x][y]:
                if visited[nx][ny] ==0:
                    heapq.heappush(queue,(-table[nx][ny],nx,ny))
                visited[nx][ny] += visited[x][y]
    return visited[n-1][m-1]
input = sys.stdin.readline
n,m = map(int,input().split())
table = [list(map(int,input().split()))for _ in range(n)]
print(BFS())


# short coding
# import heapq
# n,m=map(int,input().split())
# a=[list(map(int,input().split()))for _ in range(n)]
# q=[(a[0][0],0,0)]
# d=[(1,0),(-1,0),(0,1),(0,-1)]
# v=[[0]*m for _ in range(n)]
# v[0][0]=1
# while q:
#     h,x,y=heapq.heappop(q)
#     for g,h in d:
#         e=g+x
#         f=h+y
#         if 0<=e<n and 0<=f<m and a[e][f]<a[x][y]:
#             if v[e][f]==0:
#                 heapq.heappush(q,(-a[e][f],e,f))
#             v[e][f]+=v[x][y]
# print(v[n-1][m-1])