import sys
import heapq

input = sys.stdin.readline
MOD=1000000007
n = int(input())
s = input().rstrip("\n")
ans = 0
pos_w = []
pos_h = []
h_v = []
e = [0]*(n+1)
for k,c in enumerate(s):
    if c == "W":
        pos_w.append(k)
    elif c=="H":
        pos_h.append(k)
for i in range(n-1,-1,-1):
    c = s[i]
    e[i] = e[i+1]
    if c=="E":
        e[i]+=1
for h in pos_h:
    i = e[h]
    h_v.append([h,(pow(2,i,MOD)-i-1)])
last_idx = 0
for i in range(len(h_v)-2,-1,-1):
    h_v[i][1] = (h_v[i+1][1]+h_v[i][1])%MOD
pq = []
for k,v in h_v:
    heapq.heappush(pq,(k,v))
for w in pos_w:
    while pq:
        k,v = heapq.heappop(pq)
        if k>w:
            ans+=v
            ans%=MOD
            heapq.heappush(pq,(k,v))
            break
            
print(ans)