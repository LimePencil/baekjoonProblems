import sys

input = sys.stdin.readline
n = int(input())
arr = input().split()
cnt=0
for s in arr:
    if s in ["he", "she", "him", "her"]:
        cnt+=1
print(cnt)