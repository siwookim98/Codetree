a = int(input())

for i in range(1, a+1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    # i // 8 = 몫이 짝수다? 어떻게 구함? 
    # 2, 4, 6, 8등의 몫이어야하는데
    # 나머지가 0일 필요는 없잖아 아하
    elif (i // 8) % 2 == 0:
        continue
    elif i % 7 < 4:
        continue
    print(i, end = ' ')

    