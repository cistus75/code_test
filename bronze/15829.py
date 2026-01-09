# 15829 : Hashing
# 문제가 굉장히 복잡해보였는데, 핵심인 수식만 깔끔하게 정렬하면 생각보단 풀만하다?

a = int(input())
b = input()
r = 31
m = 1234567891
sum_num = 0

for i in range(a):
    num = ord(b[i]) - 96
    sum_num += num * (r ** i)

print(sum_num % m)