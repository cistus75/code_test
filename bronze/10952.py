# 10952 : A+B - 5

# 10951과 유사하나 종료 조건이 "입력의 마지막에는 0 두 개가 들어온다."로 설정되어 있음

while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break

    print(a + b)

