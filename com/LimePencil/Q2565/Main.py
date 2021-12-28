import sys

n = int(sys.stdin.readline().rstrip("\n"))

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
arr.sort(key=lambda x:x[0])
longest = [1]*n
longest_len = 1
for a in range(1,n):
    maximum = 0
    for b in range(0,a):
        if arr[b][1] < arr[a][1]:
            if longest[b] >= maximum:
                maximum = longest[b]
    longest[a] = maximum + 1
    longest_len = max(longest_len,longest[a])
print(n-longest_len)
