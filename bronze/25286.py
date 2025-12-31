# 25286 : 11월 11일
# 딕셔너리로 1 : 31... 이런 식으로 매칭하다가 datetime을 수집한 데이터 패치 버전으로 구분할 때 사용한게 생각나 차용함.

import datetime

d = datetime.date
dt = datetime.timedelta

t = int(input())

for i in range(t):
    y, m = map(int, input().split())
    
    re = (d(y, m, m) - dt(days = m))
    
    print(re.year, re.month, re.day)

    
