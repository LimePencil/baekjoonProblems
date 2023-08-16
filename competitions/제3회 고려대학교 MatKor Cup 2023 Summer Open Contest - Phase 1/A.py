import sys


n=int(input())

print("bowling "*n)
sys.stdout.flush()

l=input().split()

for e in l:
    if e=="swimming":
        print("soccer",end=" ")
    else:
        print("swimming",end=" ")
