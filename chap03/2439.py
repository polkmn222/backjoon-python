# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

a = int(input())

# for i in range(1, a+1):
#     for j in range(a-1, i, -1):
#         print(" ", end="")
#     for k in range(1, i):
#         print("*", end="")
#     print()

for i in range(1, a+1):
    print(" " * (a - i) + "*" * i)