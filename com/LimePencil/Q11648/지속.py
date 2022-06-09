import sys

input = sys.stdin.readline
n = int(input())
count=0
while len(str(n)) !=1:
    count+=1
    new_n=1
    for c in str(n):
        new_n*=int(c)
    n=new_n
print(count)