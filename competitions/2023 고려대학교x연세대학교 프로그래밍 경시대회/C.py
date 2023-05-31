import sys
import random
def calculate_tiredness(num):
    cnt=0
    
        
    for i in range(n):
        if i==0:
            if abs(height[i+1]-height[i])>num:
                cnt+=1
        elif i>0 and i<
    return cnt

input = lambda: sys.stdin.readline().rstrip()

# n,k=list(map(int,input().split()))
# height=list(map(int,input().split()))

n=6
k=random.randint(0,n)
height=[random.randint(1,10) for _ in range(n)]

print(n,k)
print(*height)

l=0
r=1000000001

ans=float('inf')
while l<=r:
    m=(l+r)//2
    c=calculate_tiredness(m)
    if c<=k:
        ans=min(m,ans)
        r=m-1
    else:
        l=m+1
print(ans)

ans_2=float('inf')
for i in range(101):
    c=calculate_tiredness(i)
    if c<=k:
        ans_2=min(ans_2,i)
print(ans_2)
    
    
# for _ in range(100):
#     import sys
#     import random
#     def calculate_tiredness(num):
#         cnt=0
#         for i in range(n-1):
#             if abs(height[i+1]-height[i])>num:
#                 if i==0:
#                     cnt+=1
#                 cnt+=1
#         return cnt

#     input = lambda: sys.stdin.readline().rstrip()

#     # n,k=list(map(int,input().split()))
#     # height=list(map(int,input().split()))

#     n=random.randint(1,100000)
#     k=random.randint(0,n)
#     height=[random.randint(1,100) for _ in range(n)]

#     l=0
#     r=1000000001

#     ans=float('inf')
#     while l<=r:
#         m=(l+r)//2
#         c=calculate_tiredness(m)
#         if c<=k:
#             ans=min(m,ans)
#             r=m-1
#         else:
#             l=m+1

#     ans_2=float('inf')
#     for i in range(101):
#         c=calculate_tiredness(i)
#         if c<=k:
#             ans_2=min(ans_2,i)
#     if ans!=ans_2:
#         print(ans,ans_2)