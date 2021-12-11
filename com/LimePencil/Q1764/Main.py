import sys

n, m = list(map(int,sys.stdin.readline().strip('\n').split(" ")))

dt = set()
ans = []
fin = ""
count = 0
for i in range(n):
    dt.add(sys.stdin.readline().strip('\n'))
for j in range(m):
    a = sys.stdin.readline().strip('\n')
    if a in dt:
        ans.append(a)
        count += 1
ans.sort()
fin = str(count) + "\n"
for x in ans:
    fin += x + "\n"
sys.stdout.write(fin)
