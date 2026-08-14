A_math, A_eng = map(int, input().split())
B_math, B_eng = map(int, input().split())
print(int(A_math > B_math and A_eng > B_eng))
