import sys

input = lambda: sys.stdin.readline().rstrip()
dp=[0,0,1]
for a in range(3,5001):
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

for _ in range(int(input())):
    n = int(input())
    if dp[n]!=0:
        print("First")
    else:
        print("Second")