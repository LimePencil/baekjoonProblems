import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
dp=[0,0,1]
for a in range(3,n+1):
    poss=set()
    for b in range(a-1):
        poss.add(dp[b]^dp[a-2-b])
    poss=sorted(list(poss))
    for i in range(len(poss)):
        if i!=poss[i]:
            dp.append(i)
            break
    else:
        dp.append(len(poss))
if dp[n]!=0:
    print(1)
else:
    print(2)
