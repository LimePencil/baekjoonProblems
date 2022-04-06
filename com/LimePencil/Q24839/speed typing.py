import sys

input = sys.stdin.readline
t= int(input())
for a in range(1,t+1):
    ans = 0
    i = input().rstrip("\n")
    p = input().rstrip("\n")
    index = 0
    for k,c in enumerate(i):
        found = p.find(c,index)
        if found == -1:
            ans = "IMPOSSIBLE"
            break
        else:
            ans += found - index
            index= found +1
    if ans!= "IMPOSSIBLE":
        ans+=len(p)-index
    print("Case #{}: {}".format(a,ans))