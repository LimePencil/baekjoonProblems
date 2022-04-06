import sys

input = sys.stdin.readline
t= int(input())
for a in range(1,t+1):
    ans = 0
    n = input().rstrip("\n")
    sum = 0
    for c in n:
        sum += int(c)
    mod = 9-sum%9
    mod%=9
    if mod ==0:
        ans = n[0] +"0"+n[1:] 
    else:
        found = False
        for i in range(0,len(n)):
            if int(n[i]) >mod:
                found = True
                ans = n[0:i] + str(mod) + n[i:]
                break
        if not found:
            ans = n+str(mod)
    print("Case #{}: {}".format(a,ans))