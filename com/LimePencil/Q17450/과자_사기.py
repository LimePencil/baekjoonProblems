import sys

input = sys.stdin.readline
snacks=[list(map(int,input().split())) for _ in range(3)]
ans=[]
name=["S","N","U"]
for i in range(3):
    ans.append(snacks[i][1]*10/(snacks[i][0]*10-500 if snacks[i][0]*10>=5000 else snacks[i][0]*10))
print(name[ans.index(max(ans))])