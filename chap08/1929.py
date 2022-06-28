"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""
a, b = input().split()
a = int(a)
b = int(b)

for i in range(a, b+1):
    c = 0

    for j in range(1, int(i**(1/2))+1):
        if i % j == 0:
            c += 1
        if c >= 2:
            break

    if c == 1 and i != 1:
        print(i)



"""
import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


a, b = input().split()
a = int(a)
b = int(b)

for i in range(a, b+1):
    if is_prime_number(i):
        print(i)
"""


        
