# 변수 선언 및 입력:
a, b = map(int, input().split())

# 3, 6, 9 숫자가 단 하나라도 포함되었는지 확인
def contains_369(n):
    # 계속 10으로 나눠주며 일의 자리를 조사한다.
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True

        n //= 10
    
    return False

def is_magic_number(n):
    return (n % 3 == 0) or contains_369(n)

cnt = 0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt += 1

print(cnt)