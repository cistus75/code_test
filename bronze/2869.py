# 2869 : 달팽이는 올라가고 싶다
# 처음엔 반복문으로 시도했는데, 0.25초라 시간 초과됨. 시간 복잡도 신경 써서 풀어야하는 문제라 수식으로 해결해야함.

import math
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

print(math.ceil((v - b) / (a - b)))

