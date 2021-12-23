import sys

original = [1,1,2,2,2,8]
a = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
for i in range(6):
    a[i] = original[i]-a[i]
print(*a)