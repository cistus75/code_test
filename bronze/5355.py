# 5355 : 화성 수학

t = int(input())

for _ in range(t):
    a = list(input().split())
    re = float(a[0])

    for i in range(1, len(a)):
        if a[i] == '@':
            re = re *   3
        elif a[i] == '%':
            re = re + 5
        elif a[i] == '#':
            re = re - 7
            
    print(f"{re:.2f}")



