import sys

n = int(sys.stdin.readline())
total =0
for i in range(1,n+1):
    while i%5 == 0:
        i/=5
        total +=1
print(total)
