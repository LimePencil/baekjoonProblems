import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s=input()
ans=float('inf')
# red to left
part_of_big_group=False
cnt=0
for i in range(n):
    if s[i]=="R":
        if i==0:
            part_of_big_group=True
        elif part_of_big_group:
            continue
        else:
            cnt+=1
    else:
        part_of_big_group=False
ans=min(ans,cnt)

# red to right
part_of_big_group=False
cnt=0
for i in range(n-1,-1,-1):
    if s[i]=="R":
        if i==n-1:
            part_of_big_group=True
        elif part_of_big_group:
            continue
        else:
            cnt+=1
    else:
        part_of_big_group=False
ans=min(ans,cnt)
# blue to left
part_of_big_group=False
cnt=0
for i in range(n):
    if s[i]=="B":
        if i==0:
            part_of_big_group=True
        elif part_of_big_group:
            continue
        else:
            cnt+=1
    else:
        part_of_big_group=False
ans=min(ans,cnt)

# blue to right
part_of_big_group=False
cnt=0
for i in range(n-1,-1,-1):
    if s[i]=="B":
        if i==n-1:
            part_of_big_group=True
        elif part_of_big_group:
            continue
        else:
            cnt+=1
    else:
        part_of_big_group=False
ans=min(ans,cnt)
print(ans)