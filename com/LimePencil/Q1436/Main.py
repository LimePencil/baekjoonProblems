import sys

num = int(sys.stdin.readline())
ans = 0
count = 0
i = 666
while count != num:
    s = str(i)
    if s.find("666") != -1:
        ans = i
        count +=1
    i +=1
print(ans)