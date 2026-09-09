# 5행 3열의 소문자 알파벳 배열은 어떻게 입력받을까? arr = [list(map(str, input())) for _ in range(n)]
# 소문자를 대문자로 바꾸는 함수는 무엇일까? .capitalize()
# 2중 리스트를 2차원 행렬로 프린트하는 방법은 무엇일까?

n = 5
arr = [input().upper() for _ in range(n)]

for row in arr:
    print(row)