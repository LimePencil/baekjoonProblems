import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    print("String #{}".format(t))
    s=input().rstrip()
    new=""
    for c in s:
        if c=="Z":
            new+="A"
        else:
            new+=chr(ord(c)+1)
    print(new)
    print()