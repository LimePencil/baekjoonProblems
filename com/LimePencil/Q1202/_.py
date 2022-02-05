import sys
import heapq

n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
bags = []
jewels = []
for _ in range(n):
    jewels.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
for _ in range(k):
    bags.append(int(sys.stdin.readline().rstrip("\n")))
bags.sort()
jewels.sort(key=lambda x: (x[0],-x[1]))
maximum = 0
pq = []
i = 0
w,p = jewels[i]
for b in bags:
    while i<n and w<=b:
        heapq.heappush(pq,-1*p)
        i+=1
        if i<n:
            w,p = jewels[i]
        else:
            break
    if len(pq) != 0:
        maximum += -1*heapq.heappop(pq)
print(maximum)


