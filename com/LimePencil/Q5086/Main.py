import sys

while True:
    f, s = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    if(f==0 and s==0):
        break
    if(f < s and s%f == 0):
        print("factor")
    elif(f>s and f%s == 0):
        print("multiple")
    else:
        print("neither")
