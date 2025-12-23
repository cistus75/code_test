# 8958 : OX퀴즈

   
a = int(input())

for i in range(a):
    b = input()
    s = 0
    t = 0

    for j in b:
        if j == "O":
            s += 1
            t += s
        
        elif j == "X":
            s = 0
    
    print(t)