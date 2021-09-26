import sys
from collections import deque

n = int(sys.stdin.readline())
deck = deque(list(range(1, n+1)))
for i in range(n-1):
    deck.popleft()
    deck.append(deck.popleft())
print(str(deck.pop()))
    