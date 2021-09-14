import sys

n = int(sys.stdin.readline().strip('\n'))
word = []
for i in range(n):
    word.append(sys.stdin.readline().strip('\n'))
word.sort(key=lambda x: (len(x), x))
ans = ""
prev = ""
for i in word:
    if(prev != i):
        ans += i + '\n'
    prev = i
sys.stdout.write(ans)
