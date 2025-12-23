# 2675 : 문자열 반복

t = int(input())

for i in range(t):
    r, s = input().split()

    for j in range(len(s)):
        print(s[j] * int(r), end = '')
    print()     


# 되게 c같은 스타일로 푼 느낌. 파이썬은 문자열 자체를 참조 가능하므로 굳이 인덱스가 필요없을지도?


t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)

    txt = "" 
    for j in range(s):
        txt += j * r
        
    print(txt)


# 위 코드 왜 안되는지 했더니 무의식적으로 range로 해서 오류 발생. 문자열 자체를 사용하도록 하단과 같이 수정.


t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    
    txt = "" 
    for j in s:
        txt += j * r
        
    print(txt) 
    