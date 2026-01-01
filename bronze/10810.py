# 10810 : 공 넣기


n, m = map(int, input().split())
box = n * [0]

for i in range(m):
    a, b, c = map(int, input().split())
    
    for j in range(a - 1, b):
        box[j] = c

for k in box:
    print(k, end = ' ')
