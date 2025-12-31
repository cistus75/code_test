# 5928 : Contest Timing


start = 11 * 1440 + 11 * 60 + 11

a, b, c = map(int, input().split())

end = a * 1440 + b * 60 + c


if end - start < 0:
    print(-1)

else:
    print(end - start)
    