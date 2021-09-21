import sys

n = int(sys.stdin.readline())

people = []
for i in range(n):
    people.append(sys.stdin.readline().strip('\n').split(" "))
    people[i][0] = int(people[i][0])
people.sort(key=lambda x: x[0])
ans =""
for s in people:
    ans += str(s[0]) + " " + str(s[1]) + "\n"
print(ans)