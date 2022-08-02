# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

a = int(input())
b = list(map(int, input().split()))
b.sort()

print(b[0], b[a-1])