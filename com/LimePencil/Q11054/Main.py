import sys

n = int(sys.stdin.readline().rstrip("\n"))

arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
longest_1 = [1]*n
longest_2 = [1]*n
ans = 0
for a in range(1,n):
    maximum_1 = 0
    for b in range(a):
        if arr[b] < arr[a] and longest_1[b] >= maximum_1:
            maximum_1 = longest_1[b]
    longest_1[a] = maximum_1 + 1
for a in range(n-2,-1,-1):
    maximum_2 = 0
    for b in range(a+1,n):
        if arr[b] < arr[a] and longest_2[b] >= maximum_2:
            maximum_2 = longest_2[b]
    longest_2[a] = maximum_2 + 1
for a in range(n):
    ans = max(ans,longest_1[a]+longest_2[a]-1)
print(ans)