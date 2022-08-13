import sys

input = sys.stdin.readline
n = int(input())
arr=set(int(input()) for _ in range(n))
target=set(range(1,max(arr)+1))
result=target-arr
if len(result)==0:
    print("good job")
else:
    result=sorted(list(result))
    for i in result:
        print(i)