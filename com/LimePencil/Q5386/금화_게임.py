import sys

input = lambda: sys.stdin.readline().rstrip()
for i in range(int(input())):
    s,k=map(int,input().split())
    if k%2==1:
        print(s&1)
    else:
        r=s%(k+1)
        if r==k:
            print(k)
        else:
            print(r%2)
            

# def mex(p):
#     for i in range(len(p)):
#         if i!=p[i]:
#             return i
#     return len(p)

# dp=[0]*100
# k=16
# for i in range(1,100):
#     s=set()
#     for j in range(10):
#         if k**j<=i:
#             s.add(dp[i-k**j])
#         else:
#             break
#     dp[i]=mex(sorted(list(s)))
# print(dp)