import sys

input = sys.stdin.readline
n = input().rstrip()
alp=[0]*26
for c in n:
    alp[ord(c)-97]+=1
print(*alp)