import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for _ in range(n):
    name,score = input().split()
    score=int(score)
    letter=""
    if score<60:
        letter="F"
    elif score<67:
        letter="D"
    elif score<70:
        letter="D+"
    elif score<77:
        letter="C"
    elif score<80:
        letter="C+"
    elif score<87:
        letter="B"
    elif score<90:
        letter="B+"
    elif score<97:
        letter="A"
    else:
        letter="A+"
    print(name,letter)