# 30802 : 웰컴 키트

n = int(input())
s = list(map(int, input().split()))
t, p = map(int, input().split())

total_t = 0

for i in s:
    if i == 0:
        continue
    
    elif i <= t:
        total_t += 1

    elif i % t == 0:
        total_t += i // t
    
    else:
        total_t += i // t + 1


pens = n // p
pen = n % p


print(total_t)
print(pens, pen)