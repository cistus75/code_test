# 10989 : 수 정렬하기 3
# 1번 시도는 메모리 초과남. 아예 접근 자체를 바꿔야 한다고 판단함. sort 자체를 쓰면 안되는 듯?
# 메모리 초과로 막힌게 처음이라 굉장히 당황스러웠다. https://wikidocs.net/21057 다음을 참고함.
# 서칭을 좀 해보니 계수 정렬이라는 것에 대해 알게 되었음. 신기한 방법이네. 메모리 줄이는 일종의 테크닉?

# 1번 코드. 메모리 초과로 실패

n = int(input())
num_list = []

for i in range(n):
    a = int(input())
    num_list.append(a)

sort_list = sorted(num_list)

for j in sort_list:
    print(int(j))


# 2번 코드. 계수 정리를 이용하여 메모리를 줄임. 한정된 범위라면 유용할 듯.

import sys
input = sys.stdin.readline

num = [0] * 10001

n = int(input())

for i in range(n):
    a = int(input())
    num[a] += 1

for j in range(10001):
    if num[j] != 0:

        for k in range(num[j]):
            print(j)

