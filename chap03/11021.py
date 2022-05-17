# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a = int(input())

for i in range(1, a+1):
    b, c = input().split()
    b = int(b)
    c = int(c)
    print(f'Case #{i}: {b + c}')