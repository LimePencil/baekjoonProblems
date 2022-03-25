from collections import defaultdict
import sys
import heapq
from heapq import heappush, heappop

def remove_from_heapq(l,remove,sign):
    while l and sign*l[0] in remove:
        a = heapq.heappop(l)
        remove[sign*a]-=1
        if not remove[sign*a]:
            del remove[sign*a]
        

input = sys.stdin.readline
t = int(input())
for i in range(1,t+1):
    ans = 0
    d,n,k = list(map(int,input().split()))
    attractions =[]
    for _ in range(n):
        h,s,e = list(map(int,input().split()))
        attractions.append((s,True,h))
        attractions.append((e+1,False,h))
    attractions.sort()
    top_attraction = []
    rest_attraction = []
    current_happiness = 0
    length = 0
    remove = defaultdict(int)
    for _, is_s, happy in attractions:
        if is_s:
            heapq.heappush(top_attraction,happy)
            current_happiness+=happy
            length +=1
            if length == k+1:
                value = heapq.heappop(top_attraction)
                current_happiness -= value
                length -=1
                heapq.heappush(rest_attraction,-value)
            ans = max(ans,current_happiness)
        else:
            remove[happy] +=1
            if not rest_attraction or -rest_attraction[0]<happy:
                current_happiness -=happy
                length-=1
                if rest_attraction:
                    value= -heapq.heappop(rest_attraction)
                    heapq.heappush(top_attraction,value)
                    current_happiness+=value
                    length+=1
        remove_from_heapq(rest_attraction,remove,-1)
        remove_from_heapq(top_attraction,remove,1)
    print("Case #{}: {}".format(i,ans))