# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True:
    try:
        b, c = input().split()
        b = int(b)
        c = int(c)
        print(b + c)
    except:
        break
