# 31994 : 강당 대관


list = []

for i in range(7):
    a, b = input().split()
    list.append((int(b), a))

c = max(list)

print(c[1])



    