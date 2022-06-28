"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""


def prime(a):
    if a < 2:
        return 0
    i = 2
    while i * i <= a:
        if a % i == 0:
            return 0
        i += 1
    return 1


a = int(input())
answer = 0
b = map(int, input().split(" "))
c = list(b)
for i in c:
    answer += prime(i)
print(answer)

# def pn(x):
#     if x < 2:
#         return 0
#     for j in range(2, x):
#         if x % j == 0:
#             return False
#     return True
#
#
# a = int(input())
# print(a)
# # b = []
# answer = 0
#
# # for i in range(a):
# b = list(map(int, input().split()))
#     # b.append(c)
# # print(c)
# # for i in b:
# #     if pn(i):
# #         answer += 1
# #
# # print(answer)
#
# for i in b:
#     if pn(i):
#         answer += 1
# # print(b)
# print(answer)