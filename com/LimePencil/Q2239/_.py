import sys
import copy

sys.setrecursionlimit(10**4)

def find_possible(pos):
    possibility = []
    for i in range(1,10):
        possible = True
        if i in ls[pos[0]]:
            possible = False
            continue
        if i in [row[pos[1]] for row in ls]:
            possible = False
            continue
        box_x = pos[0]//3
        box_y = pos[1]//3
        for a in range(box_x*3,box_x*3+3):
            for b in range(box_y*3,box_y*3+3):
                if ls[a][b] == i:
                    possible = False
                    continue
        if possible == True:
            possibility.append(i)
    return possibility

def backtracking(x):

    if len(zeroes) == x:
        ans = copy.deepcopy(ls)
        an = ""
        for c in range(9):
            an += "".join(list(map(str,ans[c]))) + "\n"
        sys.stdout.write(an)
        sys.exit()
        return
    else:
        pos = zeroes[x]
        possibility = find_possible(pos)
        if len(possibility) != 0:
            for i in possibility:
                ls[pos[0]][pos[1]] = i
                backtracking(x+1)
                ls[pos[0]][pos[1]] = 0
        




ls = [[0 for _ in range(9)] for _ in range(9)]
ans = None
zeroes = []
for i in range(9):
    line = sys.stdin.readline().strip('\n')
    for j in range(9):
        if int(line[j]) == 0:
            zeroes.append([i,j])
        else:
            ls[i][j] = int(line[j])
        

backtracking(0)
