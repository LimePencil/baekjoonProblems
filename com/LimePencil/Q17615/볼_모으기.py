import sys

input = lambda: sys.stdin.readline().rstrip()
def move_balls(type_of_ball_to_move,s):
    # To consider: red to left, red to right, blue to left, blue to right
    part_of_big_group=False
    cnt=0
    for i in range(n):
        if s[i]==type_of_ball_to_move:
            if i==0:
                part_of_big_group=True
            elif part_of_big_group:
                continue
            else:
                cnt+=1
        else:
            part_of_big_group=False
    return cnt

n = int(input())
s=input()
print(min(
    move_balls("R",s),
    move_balls("R",s[::-1]),
    move_balls("B",s),
    move_balls("B",s[::-1])))