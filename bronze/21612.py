# 21612 : Boiling Water

b = int(input())
p = P = 5 * b - 400

print(p)

if p > 100:
    print(-1)
elif p == 100:
    print(0)
elif p < 100:
    print(1)
    