# 10813 : 공 바꾸기


n, m = map(int, input().split())
box = [i for i in range(1, n + 1)]
temp = 0

for j in range(m):
    a, b = map(int, input().split())
    
    temp = box[a - 1]
    box[a - 1] = box[b - 1]
    box[b - 1] = temp

for k in box:
    print(k, end = ' ')