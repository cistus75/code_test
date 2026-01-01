# 5597 : 과제 안 내신 분..?
# all_list도 그냥 반복문으로 range(1, 31) 이랬으면 더 편했을 듯

all_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
input_list = []

for i in range(28):
    n = int(input())
    input_list.append(n)


no_list = set(all_list) - set(input_list)

sort_list = sorted(no_list)

print(sort_list[0])
print(sort_list[1])