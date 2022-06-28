"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""

a = int(input())
b = 2

"""
for i in range(2, a + 1):
    if a / i == 0:
        a = a / i
        answer.append(i)
        continue

print(answer)        
"""

while a >= b:
    if a % b == 0:
        print(b)
        a /= b
    else:
        b += 1
