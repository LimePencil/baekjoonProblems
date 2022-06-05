import sys

input = sys.stdin.readline
ans=[]
for i in range(1,6):
    if "FBI" in input():
        ans.append(str(i))
print(" ".join(ans) if len(ans)!=0 else "HE GOT AWAY!")