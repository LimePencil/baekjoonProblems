import sys

def mex(p):
    for i in range(len(p)):
        if i!=p[i]:
            return i
    else:
        return len(p)

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = list(map(int,input().split()))
fibo=[0,1]
for i in range(2,34):
    fibo.append(fibo[i-1]+fibo[i-2])
grundy_num=[0]*3000001
for i in range(1,3000000):
    p=set()
    for j in range(1,34):
        if fibo[j]<=i:
            p.add(grundy_num[i-fibo[j]])
        else:
            break
    grundy_num[i]=mex(sorted(list(p)))
x=0
for e in arr:
    x^=grundy_num[e]
if x!=0:
    print("koosaga")
else:
    print("cubelover")