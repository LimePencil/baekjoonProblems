

import sys

# def mex(p):
#     for i in range(len(p)):
#         if i!=p[i]:
#             return i
#     return len(p)

# grundy=[0]*100
# for i in range(1,100):
#     s=set()
#     for j in range(1,i+1):
#         s.add(grundy[i-j])
#     if i>=3:
#         for j in range(1,i-1):
#             for k in range(1,i-j):
#                 l=i-j-k
#                 s.add(grundy[j]^grundy[k]^grundy[l])        
#     grundy[i]=mex(sorted(s))
    
    
# print(grundy)
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
x=0
for e in arr:
    if e%8==7:
        x^=e+1
    elif e%8==0:
        x^=e-1
    else:
        x^=e
print("First" if x else "Second")
