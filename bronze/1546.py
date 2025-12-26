# 1546 : 평균

# map을 한번 사용하면 데이터가 더 없는 상태가 되므로, list로 감싸서 재사용 가능하게 할 것. 


n = int(input())
score = list(map(int, input().split()))

fake = (sum(score) / max(score) * 100) / n

print(fake)



    
