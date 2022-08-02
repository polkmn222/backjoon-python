# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# a = int(input())

# print(a)

# for i in range(a+1):
b = input()
# a = list(map(int, input().split()))
# print(a)
a = input()
# a = list(a)
# print(sum(int(a)))
a = list(map(int, a))
print(sum(a))