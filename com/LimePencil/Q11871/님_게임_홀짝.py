# import sys

# def mex(p):
#     for i in range(len(p)):
#         if i!=p[i]:
#             return i
#     else:
#         return len(p)

# input = lambda: sys.stdin.readline().rstrip()
# n = int(input())
# p = list(map(int,input().split()))
# grundy=[0]*101
# grundy[1]=1
# for i in range(3,101):
#     s=set()
#     s.add(0)
#     for j in range(2,i,2):
#         s.add(grundy[i-j])
#     grundy[i]=mex(sorted(s))
# print(grundy)


import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
p = list(map(int,input().split()))
x=0
for e in p:
    x^=(e-1)//2+e%2
print("koosaga" if x else "cubelover")