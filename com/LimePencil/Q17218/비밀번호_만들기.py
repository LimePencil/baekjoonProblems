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
num = table[l_f][l_s]
ans = []
i = l_f
j = l_s
while num !=0:
    num = table[i][j]
    above = table[i-1][j]
    left = table[i][j-1]
    if num -1 == above and num - 1 == left:
        ans.append(second[j-1])
        i-=1
        j-=1
    else:
        if above > left:
            i-=1
        else:
            j-=1
print("".join(reversed(ans)))
        
