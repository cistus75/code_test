# 2439 : 별 찍기 - 2

# 유독 별 찍기를 못하겠다. 

N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)