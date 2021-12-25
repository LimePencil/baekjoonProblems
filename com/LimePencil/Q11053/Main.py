import sys

n = int(sys.stdin.readline().rstrip("\n"))

arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
longest = [1]*n
longest_len = 1
for a in range(1,n):
    maximum = 0
    for b in range(0,a):
        if arr[b] < arr[a]:
            if longest[b] >= maximum:
                maximum = longest[b]
    longest[a] = maximum + 1
    longest_len = max(longest_len,longest[a])
print(longest_len)
