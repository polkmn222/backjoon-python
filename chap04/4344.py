# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

a = int(input())

for i in range(a):
    b = list(map(int, input().split()))
    avg = sum(b[1:])/b[0]
    c = 0
    for score in b[1:]:
        if score > avg:
            c += 1
    d = c/b[0] * 100
    print(f'{d:.3f}%')



# a = int(input())
#
# for i in range(a):
#     b = int(input())
#     c = list(map(int, input().split()))
#     su = sum(c)
#     # for j in range(b):
#     #     sum += c[j]
#     mean = su / b
#     count = 0
#     for k in range(b):
#         if c[k] > mean:
#             count += 1
#     print(count/b*100)

