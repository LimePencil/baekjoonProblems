# 뇌절 풀이

# import sys
# import heapq

# input = sys.stdin.readline
# MOD=1000000007
# n = int(input())
# s = input().rstrip("\n")
# ans = 0
# pos_w = []
# pos_h = []
# h_v = []
# e = [0]*(n+1)
# for k,c in enumerate(s):
#     if c == "W":
#         pos_w.append(k)
#     elif c=="H":
#         pos_h.append(k)
# for i in range(n-1,-1,-1):
#     c = s[i]
#     e[i] = e[i+1]
#     if c=="E":
#         e[i]+=1
# for h in pos_h:
#     i = e[h]
#     h_v.append([h,(pow(2,i,MOD)-i-1)])
# last_idx = 0
# for i in range(len(h_v)-2,-1,-1):
#     h_v[i][1] = (h_v[i+1][1]+h_v[i][1])%MOD
# pq = []
# for k,v in h_v:
#     heapq.heappush(pq,(k,v))
# for w in pos_w:
#     while pq:
#         k,v = heapq.heappop(pq)
#         if k>w:
#             ans+=v
#             ans%=MOD
#             heapq.heappush(pq,(k,v))
#             break
            
# print(ans)


# Modification from https://www.acmicpc.net/source/42292882
# 이 코드는 bennyws님이 쓰신 코드를 보고 감명받아서 설명하려고 가져왔습니다.
# 만약에 내려달라 하시면 내리겠습니다
import sys

input = sys.stdin.readline
MOD=1000000007
n = int(input())
s = input()
w=0
h=0
e=0
ans=0
for c in s:
    if c=="W":
        w+=1
    elif c=="H":
        h+=w
    elif c=="E":
        ans=(2*ans+e)%MOD
        e+=h
print(ans)
