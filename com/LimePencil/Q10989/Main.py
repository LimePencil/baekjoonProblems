import sys
n = int(sys.stdin.readline().strip('\n'))
list = [0]*10001
for i in range(n):
    list[int(sys.stdin.readline().strip('\n'))] += 1
for k, e in enumerate(list):
    if e != 0:
        for _ in range(e):
            sys.stdout.write(str(k) + "\n")
