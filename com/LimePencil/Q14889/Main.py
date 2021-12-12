import sys
from itertools import combinations

n = int(sys.stdin.readline().strip("\n"))
table = []
for _ in range(n):
    table.append(list(map(int,sys.stdin.readline().strip("\n").split(" "))))

comb = list(combinations(range(n),int(n/2)))
player_comb = list(combinations(range(int(n/2)),2))
ans = ""
low = float('inf')
for x in range(int(len(comb)/2)):
    team1 = comb[x]
    team2 = comb[len(comb)-x-1]
    team1_total = 0
    team2_total = 0
    for y in player_comb:
        team1_total += table[team1[y[0]]][team1[y[1]]] + table[team1[y[1]]][team1[y[0]]]
        team2_total += table[team2[y[0]]][team2[y[1]]] + table[team2[y[1]]][team2[y[0]]]
        pass

    low = min(low,abs(team1_total-team2_total))
    if low == 0:
        sys.stdout.write(str(low))
        sys.exit()
sys.stdout.write(str(low))