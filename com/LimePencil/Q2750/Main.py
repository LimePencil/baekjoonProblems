n = int(input())
list = [int(input()) for i in range(n)]
list.sort()
for i in range(n):
    print(list[i])