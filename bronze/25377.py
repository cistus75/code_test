# 25377 : 빵

re = []

n = int(input())

for i in range(n):
    a, b = list(map(int, input().split()))
    
    if a <= b:
        re.append(b)

if not re:
    print("-1")
else:
    print(min(re))