import sys
import heapq
input = sys.stdin.readline
n = int(input())
l_heap = []
r_heap = []
for i in range(1,n+1):
    a = int(input())
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap,-a)
    else:
        heapq.heappush(r_heap,a)
    if r_heap and  -l_heap[0] > r_heap[0]:
        a= heapq.heappop(l_heap)
        b = heapq.heappop(r_heap)
        heapq.heappush(l_heap,-b)
        heapq.heappush(r_heap,-a)
    print(-l_heap[0])