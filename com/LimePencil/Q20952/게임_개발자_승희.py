import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
remainder_to_remove=[0 for _ in range(7)]
MOD=1000000007
for e in a:
    remainder_to_remove[e%7]=1
to_add=0
to_add_remainder=0
# if remainder_to_remove 0 = not exist, 1= not yet removed, 2=removed
for i in range(m):
    target_remainder=(7-(to_add_remainder+b[i])%7)%7
    if remainder_to_remove[target_remainder]==1:
        # 모든 원소 없어지면 안되니까 확인
        if remainder_to_remove.count(1) == 1:
            continue
        remainder_to_remove[target_remainder]=2
    to_add+=b[i]
    to_add_remainder=7-target_remainder
    to_add%=MOD
        
ans=[]
for i in range(n):
    if remainder_to_remove[a[i]%7]==1:
        ans.append((a[i]+to_add)%MOD)
print(len(ans))
print(*ans)