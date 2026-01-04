# 11050 : 이항 계수 1
# (n k) 이렇게 있길래 뭔가 했더니 nCr이었다.
# 다른 풀이를 찾아보니 n이 충분히 클 경우 파스칼의 삼각형으로 해야한다는데, 나중에 찾아보는걸로.

import math
f = math.factorial

n, k = map(int, input().split())

print(f(n) // (f(n - k) * f(k)))