import sys

input = sys.stdin.readline
while True:
    arr = input().split()
    if arr==["#"]:
        break
    c=0
    d=0
    for i in arr[:-1]:
        if i in ["A","3","5","7","9"]:
            c+=1
        else:
            d+=1
    if c==d:
        print("Draw")
    elif c>d:
        print("Cheryl")
    else:
        print("Tania")