# 11800 : Tawla

# if로 수동 노가다 하다가 뭔가 아닌거 같아서 리스트 사용하려다가 리스트는 0부터 시작이라 빈값 넣던가 해야해서 걍 딕셔너리로 설정
# 딕셔너리 쓰기 귀찮아서 

one_name = {1: "Yakk", 2: "Doh", 3: "Seh", 4: "Ghar", 5: "Bang", 6: "Sheesh"}
two_name = {1: "Habb Yakk", 2: "Dobara", 3: "Dousa", 4: "Dorgy", 5: "Dabash", 6: "Dosh"}

t = int(input())

re = []

for i in range(t):
    a, b = list(map(int, input().split()))
    
    if (a == 6 and b == 5) or (a == 5 and b == 6):
        re.append("Sheesh Beesh")
    
    elif a == b:
        re.append(two_name[a])
    
    else:
        front = max(a, b)
        back = min(a, b)

        re.append(f"{one_name[front]} {one_name[back]}")

    print(f"Case {i + 1}: {re[i]}")
