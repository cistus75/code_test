# 25304 : 영수증

x = int(input())
n = int(input())
total = 0

for i in range(n):
    a, b = list(map(int, input().split()))
    total += a * b

if x == total:
    print("Yes")

else:
    print("No")