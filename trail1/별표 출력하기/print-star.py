n = int(input())

# 위쪽 삼각형 출력 (N줄)
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

# 아래쪽 역삼각형 출력 (N-1줄)
for i in range(n-1):
    for j in range(n-1-i):
        print('*', end=' ')
    print()