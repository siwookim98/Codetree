# 입력 받은 정수를 배열의 두번쨰 인덱스에 저장
n = int(input())
arr = [1, n]
cnt = 1

# 배열을 전전항과 전항을 더한 수로 채워나가고, 그 값이 100을 초과하면 while문을 탈출
while True:
    cnt += 1
    arr.append(arr[cnt - 1] + arr[cnt - 2])
    if arr[cnt] > 100:
        break

print(*arr)