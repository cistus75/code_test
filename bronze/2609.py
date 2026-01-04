# 2609 : 최대공약수와 최소공배수
# lcm 그냥 쓰려고 했는데, 3.7버전이라 존재하지 않았음 따라서 //로 해결
# 근데 사실 라이브러리 말고 함수로 구현하라는거 같음

import math

a, b = map(int, input().split())

gcd = math.gcd(a, b)
lcm = (a * b) // gcd

print(gcd)
print(lcm)