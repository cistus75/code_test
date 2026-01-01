# 10811 : 바구니 뒤집기

n, m = map(int, input().split())
box = [i for i in range(1, n + 1)]
temp = 0

for j in range(m):
    a, b = map(int, input().split())
    
    temp = box[a - 1 : b]
    temp.reverse()
    box[a - 1 : b] = temp

for k in range(n):
    print(box[k], end = ' ')