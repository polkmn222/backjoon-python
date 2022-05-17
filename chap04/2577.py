# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
#
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

a = int(input())
b = int(input())
c = int(input())

# d = a * b * c
# d = str(d)
# num = list(d)
# print(num)
#
# list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(num)):
#     if num[i] == list[0]:
#         list2.append()

d = list(str(a * b * c))
for i in range(10):
    print(d.count(str(i)))
