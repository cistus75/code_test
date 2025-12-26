# 2292 : 벌집

n = int(input())

a = 1
b = 1

while n > a:
    a += 6 * b 
    b += 1

print(b)