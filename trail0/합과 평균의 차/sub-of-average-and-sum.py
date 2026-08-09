# 첫번째 줄에 세 정수 a,b,c가 공백을 두고 주어집니다. 
a, b, c = input().split()
# 단, a,b,c의 합은 3의 배수
sumunit = int(a) + int(b) + int(c)
averageunit = sumunit/3
print(sumunit)
print(int(averageunit))
print(int(sumunit - averageunit))