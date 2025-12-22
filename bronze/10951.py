# 10951 : A+B - 4

# eof 문제. try - except나 sys.stdin.readline으로 해결. 본 문제는 입력이 작으므로 try 구문 사용

while True:
    try:
        a, b = map(int, (input().split()))
        print(a + b)
    
    except EOFError:
        break

