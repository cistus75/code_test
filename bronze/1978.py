# 1978 : 소수 찾기
# 왜 안되나 했더니 1 판정을 안해줘서 발생하는 문제. 

n = int(input())
a = list(map(int, input().split()))

def num(a):
    if a == 1:
        return False
    
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

count = 0

for j in a:
    j = int(j)
    if num(j):
        count += 1
    
print(count)
        
