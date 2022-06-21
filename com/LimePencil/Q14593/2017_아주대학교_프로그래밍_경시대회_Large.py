import sys

input = sys.stdin.readline
people= [list(map(int,input().split()))+[i+1] for i in range(int(input()))]
people.sort(key= lambda x: (x[0],-x[1],-x[2]))
print(people[-1][3])