import sys

input = sys.stdin.readline
n = int(input())
l=[i*100+99 for i in range(99,-1,-1)]
diff=float('inf')
num=0
for i in l:
    if abs(i-n)<diff:
        num=i 
        diff=abs(i-n)
print(num)