# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

a = int(input())
b = int(input())
c = b % 100 % 10
# print(c)
d = b % 100 - c
# print(d)
e = b - c - d
# print(e)
print(a * c)
print(int(a * d / 10))
print(int(a * e / 100))
print(a * b)