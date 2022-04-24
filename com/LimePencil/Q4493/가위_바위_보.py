import sys

input = sys.stdin.readline
for _ in range(int(input())):
    win_a=0
    win_b=0
    for _ in range(int(input())):
        a,b=input().split()
        if (a==b):
            continue
        elif (a=="R" and b=="S") or (a=="S" and b=="P") or (a=="P" and b=="R"):
            win_a+=1
        else:
            win_b+=1
    print("Player 1" if win_a>win_b else "Player 2" if win_b>win_a else "TIE")