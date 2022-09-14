import sys

input = sys.stdin.readline
n = int(input())
ans=[input().rstrip() for _ in range(n)]
ques=[input().rstrip() for _ in range(n)]
cnt=0
for i in range(n):
    if ans[i]==ques[i]:
        cnt+=1
print(cnt)