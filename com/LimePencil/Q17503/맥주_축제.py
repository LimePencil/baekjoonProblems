import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
n,m,k = map(int,input().split())
ans=-1
beer=[]
for _ in range(k):
    v,c = map(int,input().split())
    beer.append((v,c))
beer.sort(key=lambda x: (x[1],-x[0]))
beers_to_drink=[]
amount_of_like=0
for i in range(k):
    v,c=beer[i]
    amount_of_like+=v
    heapq.heappush(beers_to_drink,(v,c))
    if len(beers_to_drink)>n:
        v2,c2=heapq.heappop(beers_to_drink)
        amount_of_like-=v2
    if len(beers_to_drink)==n and amount_of_like>=m:
        print(c)
        break
else:
    print(ans)