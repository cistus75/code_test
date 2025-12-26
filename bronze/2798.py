# 2798 : 블랙잭 

from itertools import combinations

n, m = map(int, input().split())
num = list(map(int, input().split()))

best = 0

for i in combinations(num, 3):
    now = sum(i)

    if now <= m:
        best = max(best, now)

print(best)