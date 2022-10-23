import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
hq=[]
for _ in range(n):
    arr = list(map(int,input().split()))
    for a in arr:
        heapq.heappush(hq,a)
        if len(hq)>n:
            heapq.heappop(hq)
print(heapq.heappop(hq))