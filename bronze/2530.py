# 2530 : 인공지능 시계
# 따로 나눠서 계산하는 식으로 하다 지나치게 복잡해져 통합해서 연산하기로 함

a, b, c = map(int, input().split())
d = int(input())

sec = a * 3600 + b * 60 + c + d
sec = sec % 86400

now_a = sec // 3600
now_b = (sec % 3600) // 60
now_c = sec % 60


print(now_a, now_b, now_c)