import sys

n = int(sys.stdin.readline().rstrip("\n"))
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
ans = [-1]*n

stack = []
for k, i in enumerate(arr):
    while len(stack) > 0 and arr[stack[-1]] <i:
        ans[stack.pop()] = i
    stack.append(k)
print(*ans)
