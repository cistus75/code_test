# 2908 : 상수

a, b = map(int, input().split())

re_a = int(str(a)[::-1])
re_b = int(str(b)[::-1])

print(max(re_a, re_b))