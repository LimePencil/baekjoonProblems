import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
rooms=[]
by_start=[]
for _ in range(n):
    num,s,e = list(map(int,input().split()))
    heapq.heappush(by_start,(s,e))
ans=0
for _ in range(n):
    prev_class=-1
    s,e=heapq.heappop(by_start)    
    while len(rooms)>0 and  rooms[0]<=s:
        heapq.heappop(rooms)
    heapq.heappush(rooms,e)
    ans=max(ans,len(rooms))
print(ans)