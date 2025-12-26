# 2480 : 주사위 세개

# if else 노가다가 아니라 좀 더 효율적으로 풀 수 있는 방법이 있긴 할 듯? elif 조건도 좀 더 단순화 가능할 듯 싶음.


a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + (a * 1000))

elif a == b:
    print(1000 + (a * 100)) 

elif a == c:
    print(1000 + (a * 100)) 

elif b == c:
    print(1000 + (b * 100)) 

else:
    print(100 * max(a, b, c))




