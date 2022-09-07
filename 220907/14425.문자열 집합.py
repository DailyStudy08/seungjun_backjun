import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

set_s = set(input() for _ in range(N))
check = list(input() for _ in range(M))

cnt = 0
for i in set_s:
    for j in check:
        if i == j:
            cnt += 1
print(cnt)