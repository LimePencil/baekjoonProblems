import sys

input = sys.stdin.readline
n = int(input())
weights = list(map(int,input().split()))
possible_weight = set()
for w in weights:
    to_be_added = set()
    to_be_added.add(w)
    for v in possible_weight:
        to_be_added.add(v+w)
        to_be_added.add(abs(v-w))
    possible_weight= possible_weight|to_be_added
m = int(input())
marbles = list(map(int,input().split()))
ans = []
for m in marbles:
    if m in possible_weight:
        ans.append("Y")
    else:
        ans.append("N")
print(*ans)