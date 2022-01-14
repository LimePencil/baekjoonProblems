import sys

n= int(sys.stdin.readline().rstrip("\n"))
closest = float('inf')
arr = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
a = 0
b = n-1
a_f = arr[a]
b_f = arr[b]
while a != b:
    now = arr[a] + arr[b]
    if abs(closest) > abs(now):
        a_f = arr[a]
        b_f = arr[b]
        closest = now
    if now > 0:
        b-=1
    elif now < 0:
        a+=1
    else:
        break

print(str(a_f) +  " " + str(b_f))

