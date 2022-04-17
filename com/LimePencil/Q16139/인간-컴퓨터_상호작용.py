import sys

input = sys.stdin.readline
s=input().rstrip("\n")
prefix_sum=[[0]*(len(s)+1) for _ in range(26)]
for k,i in enumerate(s):
    for j in range(26):
        prefix_sum[j][k+1]=prefix_sum[j][k]+(1 if ord(i)-97==j else 0)      
q = int(input())
for _ in range(q):
    a,l,r=input().split()
    l=int(l)
    r=int(r)
    idx=ord(a)-97
    print(prefix_sum[idx][r+1]-prefix_sum[idx][l])