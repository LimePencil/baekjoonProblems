import sys

dictionary = {}
n = int(sys.stdin.readline())
n_list = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
for i in n_list:
    if i in dictionary:
        dictionary[i] +=1
    else:
        dictionary[i] = 1
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().strip("\n").split(" ")))
ls = []
for x in m_list:
    if x in dictionary:
        ls.append(str(dictionary[x]))
    else:
        ls.append("0")
print(" ".join(ls))