import sys

while(True):
    a = sys.stdin.readline().strip('\n')
    if(a == "0"):
        break
    if(a == a[::-1]):
        print("yes")
    else:
        print("no")