# 2775 : 부녀회장이 될테야

t = int(input())

for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호

    f_0 = [a for a in range(1, n + 1)]

    for _ in range(k):
        for j in range(1, n):
            f_0[j] += f_0[j - 1]

    print(f_0[-1])

