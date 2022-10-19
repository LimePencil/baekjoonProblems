import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = Counter(map(int,input().split()))
new_arr=[]
for k,v in arr.items():
    new_arr.append(k)
    if v>=2:
        new_arr.append(k)
m=0
for i in range(len(new_arr)):
    for j in range(i+1,len(new_arr)):
        m=max(m,sum(list(map(int,list(str(new_arr[i]*new_arr[j]))))))
print(m)