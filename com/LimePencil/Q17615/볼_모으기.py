import sys

input = lambda: sys.stdin.readline().rstrip()
def move_balls(type_of_ball_to_move,s):
    s=s.lstrip(type_of_ball_to_move)
    return s.count(type_of_ball_to_move)

n = int(input())
s=input()
# To consider: red to left, red to right, blue to left, blue to right
print(min(
    move_balls("R",s),
    move_balls("R",s[::-1]),
    move_balls("B",s),
    move_balls("B",s[::-1])))