import sys

first = sys.stdin.readline().rstrip("\n")
second = sys.stdin.readline().rstrip("\n")
l_f = len(first)
l_s = len(second)
table = [[0 for i in range(l_s + 1)] for j in range(l_f+1)]
for i in range(1,l_f+1):
    for j in range(1,l_s+1):
        if second[j-1] == first[i-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])
print(table[l_f][l_s])