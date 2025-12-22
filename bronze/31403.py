# 31403 : a + b - c

# 진짜 개빡통 이슈로 처음에 int(b) + int(c) 이래서 틀림 와 진짜.

a = input()
b = input()
c = input()

print(int(a) + int(b) - int(c))
print(int(a + b) - int(c))


