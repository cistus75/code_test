# 11720 : 숫자의 합 

# 코드가 비효율적, 추후 개선해서 ver.2로 다시 해볼 것. 
# sum이랑 map 쓰면 되는데 왜 이렇게 했지? 

N = int(input())
a = list(input())
s = 0

for i in range(N):
    b = int(a[i])
    s += b


print(s)


# ver.2

a = input()
s = sum(map(int, input()))
print(s)


# ver.3
# 어차피 n 받는거 안쓰는데 걍 input()으로 넘기고, print 한줄 추가하지 말고 바로 직접 하는 방향

input()
print(sum(map(int, input)))